import pyodbc
from flask import Flask, jsonify
import numpy as np
import pickle
import pandas as pd
import random

app = Flask(__name__)

# Load the pre-trained model and preprocessor
with open("C:\\Users\\PC\\OneDrive - University of Johannesburg\\Desktop\\FLASK_TASK\\model_and_preprocessor.pkl", 'rb') as file:
    model, preprocessor = pickle.load(file)

# Connection string for SQL Server
connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=localhost\\SQLEXPRESS01;Database=master;Trusted_Connection=yes;"

@app.route('/predict', methods=['GET'])
def predict():
    connection = None
    try:
        # Connect to the SQL Server database using pyodbc
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Fetch the latest user input data
        cursor.execute("SELECT TOP 1 USER_ID, CropType, FarmSize, Area, Season FROM UserInputs ORDER BY USER_ID DESC")
        last_row = cursor.fetchone()

        if not last_row:
            return jsonify({'error': 'No user input data found'}), 404

        # List of average temperatures to choose from
        avg_temps = [20, 22, 25, 28, 30]

        # Select a random temperature from the list
        selected_temp = random.choice(avg_temps)

        # Create a DataFrame with all features, including default values for missing columns
        data = {
            'Area': last_row.Area,
            'Item': last_row.CropType,  # Use 'CropType' as the 'Item' column
            'Year': 2024,
            'Unnamed: 0': 0,  # Default value for missing columns
            'average_rain_fall_mm_per_year': 500,
            'hg/ha_yield': 10,
            'pesticides_tonnes': 0,
            'avg_temp': selected_temp  # Use the randomly selected temperature
        }

        user_id = last_row.USER_ID  # Extract user ID

        # Convert data to DataFrame
        df = pd.DataFrame([data])

        # Apply preprocessing
        preprocessed_data = preprocessor.transform(df)

        # Make prediction using the loaded model
        prediction = model.predict(preprocessed_data)[0]

        # Prepare data to insert into PredictionResults
        prediction_value = float(prediction)
        model_used = "LinearRegression"  # Replace with actual model name
        input_data = str(data)  # Convert input data to a string format

        # Insert the prediction into the PredictionResults table
        cursor.execute(
            """INSERT INTO PredictionResults 
            (PredictionValue, ModelUsed, UserId, Context)
            VALUES (?, ?, ?, ?)""",
            prediction_value, model_used, user_id, input_data
        )
        connection.commit()

        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction_value})

    except Exception as e:
        # Handle any errors
        return jsonify({'error': str(e)}), 500

    finally:
        # Ensure the database connection is closed
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
