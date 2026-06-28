@echo off
cd /d C:\Users\Lenovo\PycharmProjects\JARVIS
call .venv\Scripts\activate.bat
python -m voice.wake_word
pause