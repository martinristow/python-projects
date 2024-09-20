import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


np.random.seed(42)
data = pd.DataFrame({
    'temperature': np.random.uniform(15, 35, 1000),
    'rainfall': np.random.uniform(50, 300, 1000),
    'humidity': np.random.uniform(30, 90, 1000),
    'yield': np.random.uniform(1000, 5000, 1000)
})

data.to_csv('synthetic_crop_data.csv', index=False)

X = data[['temperature', 'rainfall', 'humidity']]
y = data['yield']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae}")


new_data = pd.DataFrame({
    'temperature': [25],
    'rainfall': [200],
    'humidity': [60]
})
predicted_yield = model.predict(new_data)
print(f"Predict Yield: {predicted_yield}")
