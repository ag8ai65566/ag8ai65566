import { expect, test } from 'claude-code/testing'
import type { TestBody } from 'claude-code/testing'

const PANE = {
  plugin: 'voice-manager',
  component: 'Pane',
  requestId: 'voice-manager',
  props: {
    title: 'Voice Manager',
    isFocused: false,
    bodyColumns: 50,
    placement: 'dock',
    scroll: { offset: 0, bodyRows: 30 },
    view: {},
  },
} as const

const FOLDER = 'E:\\HololiveVoiceManager'

// A Windows computer whose E:\HololiveVoiceManager holds a launcher, an installer and a program one level down.
function windows(on: Parameters<TestBody>[1], runs: (readonly string[])[], store: Record<string, unknown>) {
  on('command.register', () => ({ value: { command: 'voice-manager' } }))
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('session.start', (_, e) => ({ cwd: e.cwd }))
  on('ui.toast', () => ({ value: undefined }))
  on('fs.exists', (_, e) => ({ value: e.path.endsWith('C:\\Windows') || e.path.includes(FOLDER) }))
  // the test runs on Linux, where E:\… is a relative path the engine resolves from the mod's folder: match the end
  on('fs.list', (_, e) => ({
    value: e.path.endsWith(FOLDER)
      ? [{ name: '啟動 Voice Manager.bat', kind: 'file', size: 1, mtimeMs: 0, isLink: false },
        { name: 'install.bat', kind: 'file', size: 1, mtimeMs: 0, isLink: false },
        { name: 'app', kind: 'dir', size: 0, mtimeMs: 0, isLink: false }]
      : e.path.endsWith(`${FOLDER}\\app`) ? [{ name: 'VoiceManager.exe', kind: 'file', size: 1, mtimeMs: 0, isLink: false }] : [],
  }))
  on('process.run', (_, e) => {
    runs.push(e.argv)
    return { value: { exitCode: 0, stdout: '', stderr: '', isStdoutTruncated: false, isStderrTruncated: false } }
  })
  on('store.get', (_, e) => ({ value: store[e.key] }))
  on('store.set', (_, e) => { store[e.key] = e.value; return { value: undefined } })
}

test('the first press lists the programs; the one chosen opens, and opens straight away after that', async ($, on) => {
  const runs: (readonly string[])[] = []
  const store: Record<string, unknown> = {}
  windows(on, runs, store)
  await $.session.start({ cwd: '/', surface: 'desktop', isInteractive: true })

  for (const surface of ['desktop', 'terminal'] as const) {
    const ui = await $.ui.mount({ ...PANE, surface })
    if (surface === 'desktop') {
      await ui.press({ key: 'open' })
      expect(runs.length).toBe(0)                         // two programs found: the person chooses
      expect((await ui.find({ type: 'Text', text: /按一下要開啟/ }))).toBeTruthy()
      await ui.press({ key: 'pick-0' })                   // the launcher comes first, the installer is left out
      expect(runs[0]).toEqual(['cmd', '/c', 'start', '', `${FOLDER}\\啟動 Voice Manager.bat`])
      expect(store.target).toBe(`${FOLDER}\\啟動 Voice Manager.bat`)
    } else {
      await ui.press({ key: 'open' })                     // remembered: one press opens it
      expect(runs.length).toBe(2)
      expect(runs[1]).toEqual(runs[0])
    }
    await ui.unmount()
  }
})

test('a cloud session says it cannot reach the computer', async ($, on) => {
  const runs: (readonly string[])[] = []
  on('command.register', () => ({ value: { command: 'voice-manager' } }))
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('session.start', (_, e) => ({ cwd: e.cwd }))
  on('fs.exists', () => ({ value: false }))
  on('fs.list', () => ({ value: [] }))
  on('store.get', () => ({ value: `${FOLDER}\\啟動 Voice Manager.bat` }))
  on('process.run', (_, e) => { runs.push(e.argv); return { value: { exitCode: 0, stdout: '', stderr: '', isStdoutTruncated: false, isStderrTruncated: false } } })
  await $.session.start({ cwd: '/', surface: 'desktop', isInteractive: true })

  const ui = await $.ui.mount({ ...PANE, surface: 'desktop' })
  await ui.press({ key: 'open' })
  expect(runs.length).toBe(0)
  expect((await ui.find({ type: 'Text', text: /雲端工作階段/ }))).toBeTruthy()
  await ui.unmount()
})
