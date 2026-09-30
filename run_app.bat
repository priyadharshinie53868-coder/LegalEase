@echo off
echo ========================================================
echo Starting LegalEase - AI-Powered Legal Document Generator
echo ========================================================

echo Activating Python Virtual Environment...
call venv\Scripts\activate

echo Launching FastAPI Backend on http://127.0.0.1:8000 ...
start "LegalEase Backend (FastAPI)" cmd /k "venv\Scripts\uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload"

timeout /t 3 >nul

echo Launching Streamlit Frontend on http://localhost:8501 ...
start "LegalEase Frontend (Streamlit)" cmd /k "venv\Scripts\streamlit run frontend/app.py"

echo ========================================================
echo LegalEase is now running!
echo Backend:  http://127.0.0.1:8000
echo Frontend: http://localhost:8501
echo ========================================================
