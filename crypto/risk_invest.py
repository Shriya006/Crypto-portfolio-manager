import pandas as pd
import numpy as np

# -------------------------------
# Load Crypto Data
# -------------------------------
def load_crypto_data():
    
    data = {
        "Date": pd.date_range(start="2024-01-01", periods=10),
        "Bitcoin": [42000,42500,43000,43500,44000,43800,44500,45000,45200,45500],
        "Ethereum": [2200,2250,2300,2280,2350,2380,2400,2450,2480,2500],
        "Solana": [90,92,95,93,98,100,102,105,108,110],
        "Cardano": [0.45,0.46,0.47,0.46,0.48,0.49,0.50,0.52,0.51,0.53]
    }

    df = pd.DataFrame(data)
    return df


# -------------------------------
# Calculate Returns
# -------------------------------
def calculate_returns(df):

    df_returns = df.drop(columns=["Date"]).pct_change().dropna()

    return df_returns


# -------------------------------
# Risk Classification
# -------------------------------
def classify_risk(volatility):

    if volatility < 0.01:
        return "Low"
    elif volatility < 0.02:
        return "Medium"
    else:
        return "High"


# -------------------------------
# Analyze Crypto Data
# -------------------------------
def analyze_crypto(df_returns):

    summary = []

    for coin in df_returns.columns:

        mean_return = df_returns[coin].mean()
        volatility = df_returns[coin].std()

        risk = classify_risk(volatility)

        summary.append({
            "Coin": coin,
            "Expected Return": mean_return,
            "Volatility": volatility,
            "Risk Level": risk
        })

    summary_df = pd.DataFrame(summary)

    return summary_df


# -------------------------------
# Investment Allocation Rules
# -------------------------------
def allocation_rules():

    return {
        "Low": 0.60,
        "Medium": 0.30,
        "High": 0.10
    }


# -------------------------------
# Calculate Investment Mix
# -------------------------------
def calculate_investment_mix(total_investment, summary, latest_prices):

    rules = allocation_rules()

    results = []

    for risk_level, weight in rules.items():

        coins = summary[summary["Risk Level"] == risk_level]

        if len(coins) == 0:
            continue

        allocation = (total_investment * weight) / len(coins)

        for _, row in coins.iterrows():

            coin = row["Coin"]
            price = latest_prices[coin]

            units = allocation / price

            results.append({
                "Coin": coin,
                "Risk Level": risk_level,
                "Allocated Amount ($)": round(allocation,2),
                "Units to Buy": round(units,6),
                "Weight (%)": weight * 100,
                "Expected Return (%)": round(row["Expected Return"]*100,2)
            })

    return pd.DataFrame(results)


# -------------------------------
# Main Program
# -------------------------------
def main():

    print("\nGenerating Investment Mix\n")

    total_investment = float(input("Enter total investment amount ($): "))

    df = load_crypto_data()

    df_returns = calculate_returns(df)

    summary = analyze_crypto(df_returns)

    latest_prices = df.iloc[-1].drop("Date")

    portfolio = calculate_investment_mix(
        total_investment,
        summary,
        latest_prices
    )

    print("\nCRYPTO PORTFOLIO RECOMMENDATION\n")

    print(portfolio)


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    main()