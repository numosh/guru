@echo off
cd /d "%~dp0"
call venv\Scripts\activate
python guru_ai.py
pause
