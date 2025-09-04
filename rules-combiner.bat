@echo off
REM Windows wrapper script for the Rules Combiner CLI

setlocal

REM Get the directory where this batch file is located
set SCRIPT_DIR=%~dp0

REM Run the Python CLI using uv run (recommended) or fallback to python
uv run python -c "import sys; sys.path.insert(0, r'%SCRIPT_DIR%src'); from rules_combiner.cli import main; main()" %* 2>nul
if errorlevel 1 (
    echo uv not found, trying with python...
    python -c "import sys; sys.path.insert(0, r'%SCRIPT_DIR%src'); from rules_combiner.cli import main; main()" %*
)

endlocal
