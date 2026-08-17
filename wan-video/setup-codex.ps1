$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path

function Say($m) { Write-Host ''; Write-Host "=== $m ===" -ForegroundColor Cyan }
function Ok($m)  { Write-Host "  OK  $m" -ForegroundColor Green }
function Warn($m){ Write-Host "  !!  $m" -ForegroundColor Yellow }
function Die($lines) {
  Write-Host ''
  foreach ($l in $lines) { Write-Host "  $l" -ForegroundColor Red }
  Write-Host ''
  Write-Host '============================================' -ForegroundColor Red
  Write-Host '  SETUP DID NOT COMPLETE - see the reason above.' -ForegroundColor Red
  Write-Host '============================================' -ForegroundColor Red
  exit 1
}

# Native tools write ordinary progress to stderr, and Windows PowerShell 5.1
# turns a redirected stderr line into a terminating error while
# $ErrorActionPreference is 'Stop'. Same trap that made a successful git pull
# look like a failed update. Exit code is the only honest signal.
function Invoke-Native {
  param([string]$Exe, [string[]]$ExeArgs)
  $prev = $ErrorActionPreference
  $ErrorActionPreference = 'Continue'
  try {
    $lines = & $Exe @ExeArgs 2>&1
    $code = $LASTEXITCODE
    $text = ''
    if ($null -ne $lines) {
      $text = (($lines | ForEach-Object { $_.ToString() }) -join "`n").Trim()
    }
    return [pscustomobject]@{ Code = $code; Text = $text }
  } finally {
    $ErrorActionPreference = $prev
  }
}

Write-Host ''
Write-Host 'Codex + Claude Code' -ForegroundColor Cyan
Write-Host 'Let Claude Code hand work to OpenAI Codex as an MCP tool.' -ForegroundColor Gray

Say 'Checking what is already here'
$npm = Get-Command npm -ErrorAction SilentlyContinue
if (-not $npm) {
  Die @(
    'npm not found. Codex ships as an npm package, so Node.js is required.',
    'Install Node.js LTS from https://nodejs.org/ then run this again.'
  )
}
Ok "npm: $((Invoke-Native 'npm' @('--version')).Text)"

$claude = Get-Command claude -ErrorAction SilentlyContinue
if (-not $claude) {
  Warn 'claude CLI not found on PATH. The Codex install below still works,'
  Warn 'but the registration step will be skipped - run it yourself afterwards:'
  Warn '    claude mcp add codex -- codex mcp-server'
} else {
  Ok 'claude CLI found'
}

Say 'Installing the Codex CLI'
$install = Invoke-Native 'npm' @('install', '-g', '@openai/codex')
if ($install.Code -ne 0) {
  Die @('npm install failed. The reason it gave:', $install.Text)
}
$codex = Get-Command codex -ErrorAction SilentlyContinue
if (-not $codex) {
  Die @(
    'codex installed but is not on PATH yet.',
    'Close this window, open a new terminal, and run this script again.'
  )
}
Ok "codex: $((Invoke-Native 'codex' @('--version')).Text)"

Say 'Sign in'
# Deliberately not automated. `codex login` opens a browser and uses your
# ChatGPT plan; the API-key path reads the key from stdin. Either way the
# credential belongs to you and should never be typed into a script, pasted
# into a chat, or committed.
$status = Invoke-Native 'codex' @('login', 'status')
if ($status.Code -eq 0 -and $status.Text -notmatch 'not logged in') {
  Ok 'Already signed in'
  Write-Host "      $($status.Text)" -ForegroundColor Gray
} else {
  Warn 'Not signed in yet. Do this yourself, in this window:'
  Write-Host ''
  Write-Host '    codex login' -ForegroundColor White
  Write-Host ''
  Write-Host '  That opens a browser and uses your ChatGPT plan - no API key needed.' -ForegroundColor Gray
  Write-Host '  If you would rather use an API key, it is read from stdin so it never' -ForegroundColor Gray
  Write-Host '  appears in your shell history:' -ForegroundColor Gray
  Write-Host ''
  Write-Host '    $env:OPENAI_API_KEY = "sk-..."   # this session only' -ForegroundColor White
  Write-Host '    $env:OPENAI_API_KEY | codex login --with-api-key' -ForegroundColor White
  Write-Host ''
}

if ($claude) {
  Say 'Registering Codex with Claude Code'
  $existing = Invoke-Native 'claude' @('mcp', 'list')
  if ($existing.Text -match 'codex') {
    Ok 'Already registered (claude mcp list already mentions codex)'
  } else {
    $add = Invoke-Native 'claude' @('mcp', 'add', 'codex', '--', 'codex', 'mcp-server')
    if ($add.Code -ne 0) {
      Warn 'Registration failed. Run it by hand to see why:'
      Warn '    claude mcp add codex -- codex mcp-server'
      Warn "Reason: $($add.Text)"
    } else {
      Ok 'Registered as MCP server "codex"'
    }
  }
}

Say 'Health check'
$doctor = Invoke-Native 'codex' @('doctor')
foreach ($line in ($doctor.Text -split "`n")) {
  if ($line -match '^\s*(\u2713|\u2717|\u26a0)') { Write-Host "  $line" }
}

Write-Host ''
Write-Host '============================================' -ForegroundColor Green
Write-Host '  CODEX SETUP OK' -ForegroundColor Green
Write-Host '============================================' -ForegroundColor Green
Write-Host ''
Write-Host 'Next: restart Claude Code, then ask it to use codex. Check with:' -ForegroundColor Gray
Write-Host '    claude mcp list' -ForegroundColor White
Write-Host ''
Write-Host 'Full notes, including what this is and is not good for:' -ForegroundColor Gray
Write-Host '    docs/codex-mcp.md' -ForegroundColor White
Write-Host ''
