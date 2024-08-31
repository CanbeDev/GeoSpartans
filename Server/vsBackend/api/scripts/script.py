import sys
import joblib  # or pickle, depending on how you saved your model

# Load your trained model
model = joblib.load('script.py')

# Retrieve the input from command-line arguments
input_data = sys.argv[1]

# Preprocess the input as needed
# ...

# Make predictions
prediction = model.predict([input_data])

# Print the result, which will be captured by ASP.NET
print(prediction[0])
