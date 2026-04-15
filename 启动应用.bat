@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Starting AI Report Generator...
start http://localhost:8503
.venv\Scripts\streamlit.exe run app.py --server.port 8503
pause
