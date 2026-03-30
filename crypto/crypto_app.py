import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("Crypto Portfolio Manager & Prediction App")

st.write("This app predicts the next 7 days crypto price trend.")

# -------------------------
# Sample crypto data
# -------------------------
prices = [42000, 42100, 42300, 42500, 42700, 42850, 43000]

data = pd.DataFrame(prices, columns=["Close"])
data["Day"] = np.arange(len(data))

# -------------------------
# Train Model
# -------------------------
X = data[["Day"]]
y = data["Close"]

model = LinearRegression()
model.fit(X, y)

# -------------------------
# Predict Future Prices
# -------------------------
future_days = np.arange(len(data), len(data)+7).reshape(-1,1)
predicted_prices = model.predict(future_days)

prediction_table = pd.DataFrame({
    "Day": range(1,8),
    "Predicted Price": predicted_prices.astype(int)
})

# -------------------------
# Display Table
# -------------------------
st.subheader("7 Day Price Prediction")
st.table(prediction_table)

# -------------------------
# Graph
# -------------------------
st.subheader("Prediction Graph")

plt.plot(range(len(data)), data["Close"], label="Past Price")
plt.plot(range(len(data), len(data)+7), predicted_prices, label="Predicted Price")

plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()

st.pyplot(plt)

# -------------------------
# Portfolio Section
# -------------------------
st.subheader("Portfolio Investment")

btc = st.slider("Bitcoin Investment (%)",0,100,40)
eth = st.slider("Ethereum Investment (%)",0,100,35)
sol = st.slider("Solana Investment (%)",0,100,25)

total = btc + eth + sol

st.write("Total Allocation:", total,"%")

if total != 100:
    st.warning("Portfolio allocation should equal 100%")
else:
    st.success("Portfolio allocation is valid")