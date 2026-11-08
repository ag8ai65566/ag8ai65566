# voice-manager

A pane on the right side of Claude with one button that opens Voice Manager on this computer.

- The first press lists the programs, batch files and shortcuts found in `E:\HololiveVoiceManager` (installers and
  updaters left out); press the one that starts Voice Manager, or paste a path or a web address. When only one is
  found, it is opened straight away.
- The choice is remembered across sessions; every press after that opens it at once. "換一個程式" changes it.
- `/voice-manager` opens the pane and presses the button.

It only works in a Claude session that runs on the Windows computer itself (the desktop app's Code tab with a local
folder, or `claude` in a terminal). A cloud session cannot reach the computer, and the pane says so.

## Install

Once, on the Windows computer: double-click `install-claude-plugin.bat` in the Voice Studio folder. It runs

```
claude plugin marketplace add "<Voice Studio folder>\claude-plugin"
claude plugin install voice-manager@voice-studio --scope user
```

The plugin is read from that folder, so `update.bat` keeps it up to date (a running Claude picks a change up with
`/reload-plugins`).
