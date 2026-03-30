import streamlit as st
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("🚀 Crypto Portfolio Manager Dashboard")

# -----------------------------------
# LIVE CRYPTO PRICES (CoinGecko API)
# -----------------------------------

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"

data = requests.get(url).json()

btc_price = data["bitcoin"]["usd"]
eth_price = data["ethereum"]["usd"]
sol_price = data["solana"]["usd"]

st.subheader("📊 Live Crypto Prices")

col1, col2, col3 = st.columns(3)

col1.metric("Bitcoin (BTC)", btc_price)
col2.metric("Ethereum (ETH)", eth_price)
col3.metric("Solana (SOL)", sol_price)

# -----------------------------------
# PORTFOLIO INPUT
# -----------------------------------

st.subheader("💼 Portfolio Allocation")

btc = st.slider("Bitcoin %",0,100,40)
eth = st.slider("Ethereum %",0,100,35)
sol = st.slider("Solana %",0,100,25)

total = btc + eth + sol

st.write("Total Allocation:", total,"%")

if total != 100:
    st.warning("⚠ Portfolio must equal 100%")

# -----------------------------------
# PORTFOLIO VALUE
# -----------------------------------

investment = st.number_input("Enter Total Investment ($)",100,100000,1000)

btc_value = investment*(btc/100)
eth_value = investment*(eth/100)
sol_value = investment*(sol/100)

portfolio_table = pd.DataFrame({
    "Crypto":["Bitcoin","Ethereum","Solana"],
    "Investment($)":[btc_value,eth_value,sol_value]
})

st.subheader("📊 Portfolio Distribution")

st.table(portfolio_table)

# -----------------------------------
# RISK ANALYSIS
# -----------------------------------

returns = np.array([0.08,0.10,0.12])  # example yearly returns
volatility = np.array([0.30,0.40,0.50])

weights = np.array([btc,eth,sol])/100

portfolio_return = np.sum(weights*returns)
portfolio_risk = np.sqrt(np.sum((weights**2)*(volatility**2)))

st.subheader("⚠ Portfolio Risk Analysis")

st.write("Expected Return:", round(portfolio_return*100,2),"%")
st.write("Risk (Volatility):", round(portfolio_risk*100,2),"%")

# -----------------------------------
# BEST ASSET MIX
# -----------------------------------

st.subheader("🤖 Suggested Asset Mix")

if portfolio_risk > 0.40:
    st.write("High Risk Portfolio → Reduce Solana allocation")

elif portfolio_risk < 0.30:
    st.write("Low Risk Portfolio → Can increase Ethereum")

else:
    st.write("Balanced Portfolio 👍")

# -----------------------------------
# PRICE PREDICTION
# -----------------------------------

st.subheader("📈 Bitcoin Price Prediction (Next 7 Days)")

prices = [42000,42100,42300,42500,42700,42850,43000]

df = pd.DataFrame(prices, columns=["Close"])
df["Day"] = np.arange(len(df))

X = df[["Day"]]
y = df["Close"]

model = LinearRegression()
model.fit(X,y)

future_days = np.arange(len(df),len(df)+7).reshape(-1,1)

predicted = model.predict(future_days)

prediction_table = pd.DataFrame({
    "Day":range(1,8),
    "Predicted Price":predicted.astype(int)
})

st.table(prediction_table)

# -----------------------------------
# DASHBOARD GRAPH
# -----------------------------------

st.subheader("📉 Price Trend Graph")

plt.plot(range(len(df)),df["Close"],label="Past Price")
plt.plot(range(len(df),len(df)+7),predicted,label="Predicted")

plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()

st.pyplot(plt)