@echo off
set VENV_DIR=.venv
set REQUIREMENTS=requirements.txt

if not exist %VENV_DIR% (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
    
    call %VENV_DIR%\Scripts\activate.bat
    
    if exist %REQUIREMENTS% (
        echo Installing requirements...
        pip install -r %REQUIREMENTS%
    )
) else (
    call %VENV_DIR%\Scripts\activate.bat
)

call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo Failed to run venv!
    pause
    exit /b 1
)
python main.py
pause
deactivate
