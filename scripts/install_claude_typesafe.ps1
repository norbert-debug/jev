$ErrorActionPreference = "Stop"

Write-Host "Installing the official TypeSafe skill for Claude Code..."
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai

Write-Host ""
Write-Host "Done. In Claude Code use: /typesafe:typesafe-ai"
Write-Host "Keep TYPESAFE_API_KEY in your environment/secret store; never commit it."
