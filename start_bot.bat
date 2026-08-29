@echo off
title Discord Auto Role Bot

cd /d "%~dp0"

echo ==============================
echo Discord Auto Role Bot
echo ==============================
echo.
echo Current folder:
cd
echo.
echo Python:
".venv\Scripts\python.exe" --version
echo.
echo Starting bot...
echo.

".venv\Scripts\python.exe" bot.py

echo.
echo ==============================
echo Python exited.
echo Exit code: %ERRORLEVEL%
echo ==============================
pause