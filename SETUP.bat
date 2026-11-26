@echo off
REM KisanTalk - Setup Script for Windows
REM This script sets up and runs the complete system

echo ====================================
echo   KisanTalk - Farmers Grievance System
echo   Quick Setup Script
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [OK] Python is installed

REM Create virtual environment
echo.
echo Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo [OK] Virtual environment created
) else (
    echo [OK] Virtual environment already exists
)

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo Installing dependencies...
cd backend
pip install -r requirements.txt
cd ..

echo.
echo ====================================
echo   Setup Complete!
echo ====================================
echo.
echo Start the system:
echo.
echo   1. Open Command Prompt in this folder
echo   2. Run: venv\Scripts\activate
echo   3. Run: cd backend
echo   4. Run: python app.py
echo.
echo   Then open in browser:
echo   - Backend: http://localhost:5000
echo   - Frontend: frontend/index.html
echo.
pause
