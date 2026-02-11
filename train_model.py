import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import joblib

# Load the dataset
data = pd.read_excel('Data_Train.xlsx')

# Data Cleaning
data.dropna(inplace=True)

# Date_of_Journey
data['Date_of_Journey'] = pd.to_datetime(data['Date_of_Journey'])
data['Journey_day'] = data['Date_of_Journey'].dt.day
data['Journey_month'] = data['Date_of_Journey'].dt.month
data.drop('Date_of_Journey', axis=1, inplace=True)

# Dep_Time
data['Dep_Time'] = pd.to_datetime(data['Dep_Time'])
data['Dep_hour'] = data['Dep_Time'].dt.hour
data['Dep_min'] = data['Dep_Time'].dt.minute
data.drop('Dep_Time', axis=1, inplace=True)

# Arrival_Time
data['Arrival_Time'] = pd.to_datetime(data['Arrival_Time'])
data['Arrival_hour'] = data['Arrival_Time'].dt.hour
data['Arrival_min'] = data['Arrival_Time'].dt.minute
data.drop('Arrival_Time', axis=1, inplace=True)

# Duration
def duration_to_min(duration):
    h = 0
    m = 0
    parts = duration.split()
    for part in parts:
        if 'h' in part:
            h = int(part.replace('h', ''))
        elif 'm' in part:
            m = int(part.replace('m', ''))
    return h * 60 + m

data['Duration_min'] = data['Duration'].apply(duration_to_min)
data.drop('Duration', axis=1, inplace=True)

# Total_Stops
data['Total_Stops'] = data['Total_Stops'].replace({'non-stop': 0, '1 stop': 1, '2 stops': 2, '3 stops': 3, '4 stops': 4})

# Drop columns
data.drop(['Route', 'Additional_Info'], axis=1, inplace=True)

# Feature Selection
X = data.drop('Price', axis=1)
y = data['Price']

# Define categorical and numerical features
categorical_features = ['Airline', 'Source', 'Destination']
numerical_features = ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour', 'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_min']

# Preprocessing Pipeline
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Model
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))])

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
print("Training the model...")
model.fit(X_train, y_train)
print("Model trained.")

# Evaluate
score = model.score(X_test, y_test)
print(f"R2 Score: {score}")

# Save Model
joblib.dump(model, 'flight_price_model.pkl')
print("Model saved as flight_price_model.pkl")
