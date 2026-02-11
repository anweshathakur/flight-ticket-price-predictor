<<<<<<< HEAD
# Flight Price Predictor

A Machine Learning powered web application that predicts flight ticket prices based on various factors like airline, source, destination, and timing.

##  Features
- **Accurate Predictions**: Uses a Random Forest Regressor model trained on historical flight data.
- **User-Friendly Interface**: Clean and modern web UI built with Flask, HTML, and CSS.
- **Real-time Inputs**: Select Airline, Source, Destination, Stops, and Travel Time to get an instant price estimate.

## Tech Stack
- **Frontend**: HTML5, CSS3 (Custom Design)
- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-Learn, Pandas, NumPy
- **Model Storage**: Joblib

## Project Structure
```
├── app.py                  # Flask backend application
├── train_model.py          # Script to train and save the ML model
├── flight_price_model.pkl  # Trained model file
├── requirements.txt        # List of dependencies
├── static/
│   └── style.css           # CSS styling for the website
├── templates/
│   └── index.html          # HTML frontend
├── Data_Train.xlsx         # Dataset used for training
└── README.md               # Project documentation
```

##  How to Run This Project

Follow these steps to set up and run the project on your local machine.

### Prerequisites
- Python 3.7 or higher installed.

### Step 1: Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone <repository-url>
cd "flight ticket price predictor"
```
*(Replace `<repository-url>` with your actual GitHub repository link)*

### Step 2: Install Dependencies
Install all the required Python libraries using pip:
```bash
pip install -r requirements.txt
```

### Step 3: Train the Model (Optional)
The project comes with a pre-trained model (`flight_price_model.pkl`). If you want to retrain it yourself:
```bash
python train_model.py
```
*Alternatively, you can open and run `train_model_fixed.ipynb` in Jupyter Notebook.*

### Step 4: Run the Application
Start the Flask web server:
```bash
python app.py
```

### Step 5: Access the Website
Open your web browser and go to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---
*Created by Anwesha Thakur*
=======
# Flight Ticket Price Prediction

A hands-on machine learning project to predict flight ticket prices based on airline,
route, stops, and travel dates, using Python and popular data science libraries.

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- matplotlib

## Project Files
- `Flight Ticket Price.ipynb` → Jupyter Notebook
- `Data_Train.xlsx` → Dataset used in the notebook
>>>>>>> 4ebfc2055f248f17bd94aa885eeaebc99240b9ac
