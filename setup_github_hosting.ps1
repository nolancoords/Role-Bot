# One-time setup: stores your Discord token as a GitHub secret and starts the bot.
# Requires the GitHub CLI (https://cli.github.com) and `gh auth login` already done.
# Run from the repo folder:  powershell -ExecutionPolicy Bypass -File .\setup_github_hosting.ps1

$ErrorActionPreference = "Stop"
$repo = "nolancoords/Role-Bot"

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "GitHub CLI (gh) not found. Install it from https://cli.github.com and run 'gh auth login'."
}

# Read the token from the local .env if present, otherwise ask for it.
$token = $null
if (Test-Path ".env") {
    $line = Get-Content ".env" | Where-Object { $_ -match '^\s*DISCORD_TOKEN\s*=' } | Select-Object -First 1
    if ($line) { $token = ($line -split '=', 2)[1].Trim().Trim('"').Trim("'") }
}
if (-not $token) {
    $secure = Read-Host "Paste your Discord bot token" -AsSecureString
    $token = [Runtime.InteropServices.Marshal]::PtrToStringAuto(
        [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure))
}

Write-Host "Saving DISCORD_TOKEN as a repository secret..."
$token | gh secret set DISCORD_TOKEN --repo $repo

Write-Host "Starting the bot workflow..."
gh workflow run "Run Role Bot" --repo $repo

Write-Host "Done. Watch it here: https://github.com/$repo/actions"
