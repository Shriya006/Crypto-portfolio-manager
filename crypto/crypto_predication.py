'''
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# ----------------------------
# Load crypto data
# ----------------------------
data = pd.read_csv("crypto_data1.csv")

# ----------------------------
# Create day index
# ----------------------------
data["Day"] = np.arange(len(data))

X = data[["Day"]]
y = data["Close"]

# ----------------------------
# Train prediction model
# ----------------------------
model = LinearRegression()
model.fit(X, y)

# ----------------------------
# Predict next 7 days
# ----------------------------
future_days = np.arange(len(data), len(data)+7).reshape(-1,1)

predicted_prices = model.predict(future_days)

# ----------------------------
# Create prediction table
# ----------------------------
prediction_table = pd.DataFrame({
    "Day": range(1,8),
    "Predicted Price": predicted_prices.astype(int)
})

# ----------------------------
# Show result
# ----------------------------
print(prediction_table)
'''

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# -----------------------------
# Sample crypto price data
# -----------------------------
prices = [42000, 42100, 42300, 42500, 42700, 42850, 43000]

# Convert to DataFrame
data = pd.DataFrame(prices, columns=["Close"])

# Create day numbers
data["Day"] = np.arange(len(data))

# Features and target
X = data[["Day"]]
y = data["Close"]

# Train model
model = LinearRegression()
model.fit(X, y)

# -----------------------------
# Predict next 7 days
# -----------------------------
future_days = np.arange(len(data), len(data) + 7).reshape(-1, 1)

predicted_prices = model.predict(future_days)

# -----------------------------
# Create prediction table
# -----------------------------
prediction_table = pd.DataFrame({
    "Day": range(1, 8),
    "Predicted Price": predicted_prices.astype(int)
})

# Print output
print(prediction_table)