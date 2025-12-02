# PowerShell script to validate the project
# Usage: .\check_project.ps1

$pythonExe = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $pythonExe)) {
    Write-Host "Virtual environment not found. Create one and install dependencies:\npython -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt" -ForegroundColor Yellow
    exit 1
}

Write-Host "Running the analysis script..." -ForegroundColor Green
& $pythonExe "run_analysis.py"
if ($LASTEXITCODE -eq 0) {
    Write-Host "Project checks completed successfully." -ForegroundColor Green
    exit 0
} else {
    Write-Host "Project checks failed. Please review the output above for errors." -ForegroundColor Red
    exit $LASTEXITCODE
}
