/** What the pane shows: the remembered program, the choices found, and the last thing that happened. */
export type View = {
  /** Where the program is looked for, the first time. */
  folder: string
  /** True while the person is choosing what the button opens. */
  isPicking: boolean
  /** Programs, batch files and shortcuts found in the folder. */
  candidates: string[]
  /** The last result or problem, shown under the button. */
  message: string
  /** False when this Claude does not run on Windows (a cloud session cannot reach the person's computer). */
  isWindows: boolean
}

declare module 'claude-code' {
  interface PluginState {
    'voice-manager': { view: Shaped<View>; target: Shaped<string> }
  }
}
