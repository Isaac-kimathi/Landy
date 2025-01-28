import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load sample land data
data = pd.read_csv('land_data.csv')

# Features and target variables
X = data[['area_sqft', 'land_type_encoded']]
y = data['price']

# # Train a simple regression model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'land_price_model.pkl')

print("Model trained and saved successfully!")
