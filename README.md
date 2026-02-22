# Flight Price Predictor

Ever wondered what your flight might cost before you even open MakeMyTrip? SkyFare is a machine learning powered web app that estimates Indian domestic flight prices based on your airline, route, stops, and time of travel — instantly, no searching required.

🌐 **Live Demo**: [flight-ticket-price-predictor.onrender.com](https://flight-ticket-price-predictor.onrender.com/)

---

## Features

- **ML-Powered Predictions** — Uses a Random Forest Regressor trained on real historical flight data
- **Smart Time Slots** — Choose from natural departure/arrival windows (Morning, Evening, Night etc.) instead of exact times
- **Instant Results** — Get a fare estimate in seconds based on your inputs
- **Clean UI** — Simple, friendly interface built with Flask, HTML, and CSS

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3 |
| Backend | Flask (Python) |
| Machine Learning | Scikit-Learn, Pandas, NumPy |
| Model Storage | Joblib |
| Deployment | Render |

---

## Project Structure

```
├── app.py                    # Flask backend + prediction logic
├── train_model.py            # Script to train and save the ML model
├── flight_price_model.pkl    # Pre-trained Random Forest model
├── requirements.txt          # Python dependencies
├── Data_Train.xlsx           # Dataset used for training
├── static/
│   └── style.css             # Frontend styling
└── templates/
    └── index.html            # Frontend UI
```

---

## Run Locally

### Prerequisites
- Python 3.7 or higher

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/anweshathakur/flight-ticket-price-predictor.git
cd flight-ticket-price-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

> The pre-trained model (`flight_price_model.pkl`) is included so you don't need to retrain. If you'd like to retrain it yourself, run `python train_model.py` or open `train_model_fixed.ipynb` in Jupyter Notebook.

---

## Dataset

Training data is sourced from `Data_Train.xlsx` and includes Indian domestic flight records with features like airline, source, destination, stops, departure time, and ticket price.

---

*Created by Anwesha Thakur*
