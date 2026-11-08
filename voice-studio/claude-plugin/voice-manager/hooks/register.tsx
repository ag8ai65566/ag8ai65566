import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type { View } from '../types'

// A pane on the right with one button that opens Voice Manager on this computer. The first press lists the
// programs, batch files and shortcuts in E:\HololiveVoiceManager to choose from; the choice is remembered
// (across sessions, in $.store), so every press after that opens it straight away. Only a Claude that runs on
// the person's Windows computer can open it: a cloud session cannot reach that computer, and says so.

const PANE = 'voice-manager'
const FOLDER = 'E:\\HololiveVoiceManager'
const LAUNCH = /\.(exe|bat|cmd|lnk|url)$/i
const URL_RX = /^https?:\/\/\S+$/i
const PREFER = /start|run|launch|open|manager|gui|app|啟動|開啟|執行/i
const AVOID = /install|setup|update|uninstall|unins|build|test|安裝|更新|移除/i
const SKIP_DIRS = /^(\.|_|node_modules$|venv$|\.venv$|__pycache__$)/i

const view = atom({ plugin: 'voice-manager', key: 'view' } as const,
  { folder: FOLDER, isPicking: false, candidates: [], message: '', isWindows: true }, { shape: 'view-1' })
const target = atom({ plugin: 'voice-manager', key: 'target' } as const, '', { shape: 'target-1' })

const join = (dir: string, name: string) => `${dir.replace(/[\\/]+$/, '')}\\${name}`
const dirOf = (p: string) => p.replace(/[\\/][^\\/]*$/, '')
const baseOf = (p: string) => p.split(/[\\/]/).pop() ?? p

async function isWindows($: EngineInterface): Promise<boolean> {
  return $.fs.exists('C:\\Windows').catch(() => false)
}

/** Programs in the folder and one level down, the likeliest first; installers and updaters left out. */
async function find($: EngineInterface, folder: string): Promise<string[]> {
  const found: { path: string; depth: number }[] = []
  const top = await $.fs.list(folder).catch(() => [])
  for (const e of top) {
    if (e.kind === 'file' && LAUNCH.test(e.name)) found.push({ path: join(folder, e.name), depth: 0 })
    else if (e.kind === 'dir' && !SKIP_DIRS.test(e.name)) {
      for (const f of await $.fs.list(join(folder, e.name)).catch(() => [])) {
        if (f.kind === 'file' && LAUNCH.test(f.name)) found.push({ path: join(join(folder, e.name), f.name), depth: 1 })
      }
    } else if (e.kind === 'other' && LAUNCH.test(e.name)) found.push({ path: join(folder, e.name), depth: 0 })
  }
  return found
    .filter(f => !AVOID.test(baseOf(f.path)))
    .sort((a, b) => a.depth - b.depth
      || Number(!PREFER.test(baseOf(a.path))) - Number(!PREFER.test(baseOf(b.path)))
      || Number(!/\.exe$/i.test(a.path)) - Number(!/\.exe$/i.test(b.path))
      || baseOf(a.path).localeCompare(baseOf(b.path)))
    .map(f => f.path)
    .slice(0, 12)
}

/** Opens a program, shortcut, batch file, folder or web address the way a double-click would. */
async function launch($: EngineInterface, what: string): Promise<void> {
  if (!(await isWindows($))) {
    await update($, view, v => ({ ...v, isWindows: false,
      message: '這個 Claude 不是在你的 Windows 電腦上執行（雲端工作階段），打不開電腦上的程式。請在電腦上的 Claude（本機工作階段）用這個面板。' }))
    return
  }
  const isUrl = URL_RX.test(what)
  if (!isUrl && !(await $.fs.exists(what))) {
    await update($, view, v => ({ ...v, message: `找不到：${what}` }))
    return
  }
  const r = await $.process.run(['cmd', '/c', 'start', '', what], isUrl ? { timeoutMs: 15000 } : { cwd: dirOf(what), timeoutMs: 15000 })
  if (r.exitCode !== 0) {
    await update($, view, v => ({ ...v, message: `開不起來：${(r.stderr || r.stdout).trim() || `結束碼 ${r.exitCode}`}` }))
    return
  }
  await update($, view, v => ({ ...v, isPicking: false, message: `已開啟 ${baseOf(what)}` }))
  $.ui.toast('已開啟 Voice Manager')
}

async function choose($: EngineInterface, what: string): Promise<void> {
  const t = what.trim().replace(/^"|"$/g, '')
  if (!t) return
  await $.store.set('target', t)
  await update($, target, () => t)
  await launch($, t)
}

async function startPicking($: EngineInterface): Promise<void> {
  const v = await read($, view)
  const candidates = await find($, v.folder)
  await update($, view, x => ({ ...x, isPicking: true, candidates,
    message: candidates.length ? '' : `在 ${x.folder} 沒找到 .exe、.bat 或捷徑，請在下面貼上要開啟的檔案路徑或網址。` }))
}

async function press($: EngineInterface): Promise<void> {
  const t = await read($, target)
  if (t) return launch($, t)
  const v = await read($, view)
  const candidates = await find($, v.folder)
  if (candidates.length === 1) return choose($, candidates[0]!)   // only one: no need to ask
  await startPicking($)
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    const saved = await $.store.get('target')
    if (typeof saved === 'string') await update($, target, () => saved)
    const win = await isWindows($)
    await update($, view, v => ({ ...v, isWindows: win }))
    await $.command.register({ name: 'voice-manager', description: '開啟 Voice Manager（右側面板）' })
    void $.ui.open({ id: PANE, title: 'Voice Manager' })
    return next(e)
  })

  on('command.run', { command: 'voice-manager' }, async $ => {
    await $.ui.open({ id: PANE, title: 'Voice Manager' })
    await press($)
    const v = await read($, view)
    return { text: v.message || 'Voice Manager 面板已開啟。' }
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text, Button, Input } = $.ui.resolve(e)
    const v = await read($, view)
    const t = await read($, target)
    return (
      <Box flexDirection="column" gap={1}>
        <Button key="open" variant="primary" onPress={() => press($)}>開啟 Voice Manager</Button>
        <Text dimColor>{t ? `會開啟：${t}` : `第一次按：從 ${v.folder} 裡選要開啟的程式，之後就記住。`}</Text>
        {v.message ? <Text>{v.message}</Text> : null}
        {v.isPicking && (
          <Box flexDirection="column" gap={1}>
            <Text>按一下要開啟的那一個：</Text>
            {v.candidates.map((c, i) => (
              <Button key={`pick-${i}`} onPress={() => choose($, c)}>{baseOf(c)} <Text dimColor>{dirOf(c)}</Text></Button>
            ))}
            <Input key="path" label="或貼上路徑／網址" placeholder="E:\HololiveVoiceManager\啟動.bat"
              onSubmit={value => choose($, value)} />
            <Button key="cancel" onPress={() => update($, view, x => ({ ...x, isPicking: false }))}>取消</Button>
          </Box>
        )}
        {!v.isPicking && t ? <Button key="change" onPress={() => startPicking($)}>換一個程式</Button> : null}
      </Box>
    )
  })
}
