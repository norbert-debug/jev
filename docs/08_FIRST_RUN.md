# First live run

## 1. Create a TypeSafe account and API key

Use the TypeSafe console linked from the official docs.

Do not paste the key into GitHub or commit it to this repository.

## 2. Claude Code setup on Windows

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install_claude_typesafe.ps1
```

Then use:

```
/typesafe:typesafe-ai
```

## 3. Set the API key for the current PowerShell session

```powershell
$env:TYPESAFE_API_KEY="<your-key>"
```

For a persistent setup, use your preferred Windows secret/environment management rather than committing a file.

## 4. Run the synthetic smoke test

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run_smoke_test.ps1
```

The test:
- processes 20 synthetic project artifacts;
- asks Choice, Noul and Score questions;
- prints the model version where exposed;
- prints latency and confidence;
- counts items that would be routed to deeper reasoning.

## 5. Review before real data

Do not run LinkedIn, Gmail, Atlas or God's Eye data until:
- the smoke test works;
- question wording has been inspected;
- private/raw data paths remain ignored by Git;
- a labelled evaluation sample is prepared.

## 6. Next live dataset

Recommended first real pilot: LinkedIn Connections/Invitations, because it provides a clear measurable classification problem and mirrors a known Jev case-study pattern.

Keep the raw export outside the public repository.
