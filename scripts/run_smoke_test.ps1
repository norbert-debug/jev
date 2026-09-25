$ErrorActionPreference = "Stop"

if (-not $env:TYPESAFE_API_KEY) {
    Write-Host "TYPESAFE_API_KEY is not set in this PowerShell session."
    Write-Host 'Set it first: $env:TYPESAFE_API_KEY="<your-key>"'
    exit 1
}

if (-not (Test-Path ".venv")) {
    py -m venv .venv
}

& .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python examples\smoke_test.py
