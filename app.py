from flask import Flask, render_template, request
import pandas as pd
import joblib
from datetime import datetime

app = Flask(__name__)

# Load the trained model
model = joblib.load('flight_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract data from form
        dep_time = request.form['Dep_Time']
        arrival_time = request.form['Arrival_Time']
        date_of_journey = request.form['Date_of_Journey']
        airline = request.form['Airline']
        source = request.form['Source']
        destination = request.form['Destination']
        total_stops = int(request.form['Total_Stops'])

        # Process Date_of_Journey
        journey_date = pd.to_datetime(date_of_journey, format="%Y-%m-%d")
        journey_day = journey_date.day
        journey_month = journey_date.month

        # Process Dep_Time
        dep_hour = int(pd.to_datetime(dep_time, format="%H:%M").hour)
        dep_min = int(pd.to_datetime(dep_time, format="%H:%M").minute)

        # Process Arrival_Time
        arrival_hour = int(pd.to_datetime(arrival_time, format="%H:%M").hour)
        arrival_min = int(pd.to_datetime(arrival_time, format="%H:%M").minute)

        # Calculate Duration
        # Simple valid logic: duration in minutes
        # Since we don't have arrival date, we assume:
        # if arrival < dep, it's next day (+24h). This is a safe heuristic for short flights or user understands inputs.
        dep_total_min = dep_hour * 60 + dep_min
        arr_total_min = arrival_hour * 60 + arrival_min
        
        if arr_total_min < dep_total_min:
            arr_total_min += 24 * 60
            
        duration_min = arr_total_min - dep_total_min

        # Create DataFrame for model
        # columns must match training data features
        
        data = {
            'Total_Stops': [total_stops],
            'Journey_day': [journey_day],
            'Journey_month': [journey_month],
            'Dep_hour': [dep_hour],
            'Dep_min': [dep_min],
            'Arrival_hour': [arrival_hour],
            'Arrival_min': [arrival_min],
            'Duration_min': [duration_min],
            'Airline': [airline],
            'Source': [source],
            'Destination': [destination]
        }
        
        df = pd.DataFrame(data)

        # Predict
        prediction = model.predict(df)
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text='Your Flight Price is Rs. {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
