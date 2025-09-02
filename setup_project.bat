@echo off
echo [✅] Creating virtual environment using Python 3.10...
py -3.10 -m venv tfenv

echo [✅] Activating environment...
call tfenv\Scripts\activate

echo [✅] Upgrading pip...
python -m pip install --upgrade pip

echo [✅] Installing requirements...
pip install flask tensorflow==2.10.0 numpy pillow

echo [🚀] Running your Flask app...
python app.py

pause
