import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import pickle  # For saving the model and preprocessor

# Load data
data_path = r"C:\Users\PC\Downloads\yield_df.csv (1)\yield_df.csv"  # Use raw string for file path
df = pd.read_csv(data_path)

# Split features and target
X = df.iloc[:, :-1]  # All columns except the last
y = df.iloc[:, -1]   # Last column

# Check data types
print(X.dtypes)

# Convert categorical features to numeric if necessary
# Example for converting categorical features:
# X['Item'] = X['Item'].astype('category').cat.codes

# Identify numeric and categorical columns
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = X.select_dtypes(include=['object']).columns.tolist()

# Preprocessing
ohe = OneHotEncoder(drop='first', sparse_output=False)  # Use dense output for easier handling
scale = StandardScaler()

preprocessor = ColumnTransformer(
    transformers=[
        ('StandardScale', scale, numeric_features),
        ('OneHotEncode', ohe, categorical_features)
    ],
    remainder='passthrough'
)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, shuffle=True)

# Preprocess the data
X_train_preprocessed = preprocessor.fit_transform(X_train)
X_test_preprocessed = preprocessor.transform(X_test)  # Use transform, not fit_transform

# Initialize and train the model
model = LinearRegression()
model.fit(X_train_preprocessed, y_train)

# Make predictions
y_pred = model.predict(X_test_preprocessed)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"R^2 Score: {r2:.2f}")

def prediction(Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item):
    # Prepare input features for prediction
    features = np.array([[Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]], dtype=object)
    # Transform features using the preprocessor
    transformed_features = preprocessor.transform(features)
    # Predict the yield
    predicted_yield = model.predict(transformed_features).reshape(-1, 1)
    return predicted_yield[0][0]

# Save model and preprocessor
with open('model_and_preprocessor.pkl', 'wb') as f:
    pickle.dump((model, preprocessor), f)
