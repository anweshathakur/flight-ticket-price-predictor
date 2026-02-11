@echo off
echo Installing required libraries...
pip install flask scikit-learn pandas numpy joblib openpyxl

echo Starting the Flight Price Prediction App...
echo.
echo Once the server starts, open your browser and go to: http://127.0.0.1:5000
echo.
python app.py
pause
