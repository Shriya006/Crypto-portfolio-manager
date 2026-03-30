import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# ------------------------------
# Prepare Time Series Data
# ------------------------------
def prepare_data(df):
    df = df.copy()
    df['Day'] = np.arange(len(df))
    return df


# ------------------------------
# Predict Future Prices
# ------------------------------
def predict_future_prices(df, days_to_predict=7):
    df = prepare_data(df)

    X = df[['Day']]
    y = df['Close']

    model = LinearRegression()
    model.fit(X, y)

    future_days = np.arange(len(df), len(df) + days_to_predict).reshape(-1, 1)

    predictions = model.predict(future_days)

    return predictions


# ------------------------------
# Portfolio Return Prediction
# ------------------------------
def predict_portfolio_return(price_data, weights, days=7):

    predicted_returns = []

    for coin, df in price_data.items():

        future_prices = predict_future_prices(df, days)

        current_price = df['Close'].iloc[-1]

        future_return = (future_prices[-1] - current_price) / current_price

        predicted_returns.append(future_return)

    predicted_returns = np.array(predicted_returns)

    portfolio_prediction = np.dot(predicted_returns, weights)

    return portfolio_prediction