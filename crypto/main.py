
from data_loader import load_crypto_data, calculate_returns
from parallel_processing import parallel_calculation
from risk_checker import check_risk_level
from alert_system import send_alert
import sqlite3
import pandas as pd
from trend_predicator import predict_portfolio_return


import numpy as np
# Initialize DB
def init_db():
    conn = sqlite3.connect("database/portfolio.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS portfolio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crypto_name TEXT,
            amount REAL
        )
    """)

    conn.commit()
    conn.close()

# Example parallel task
def calculate_mean(series):
    return series.mean()

if __name__ == "__main__":
    init_db()

    def calculate_mean(series):
        return series.mean()

if __name__ == "__main__":
    df = load_crypto_data("data/crypto_data1.csv")
    returns = calculate_returns(df)

    data_dict = {col: returns[col] for col in returns.columns}

    result = parallel_calculation(calculate_mean, data_dict)

    print("Parallel Mean Returns:")
    print(result)



    from investment_mix import (
    calculate_portfolio_return,
    calculate_portfolio_risk,
    generate_equal_weights
)



if __name__ == "__main__":
    init_db()

    df = load_crypto_data("data/crypto_data1.csv")
    returns = calculate_returns(df)

    mean_returns = returns.mean()
    covariance_matrix = returns.cov()

    weights = generate_equal_weights(len(mean_returns))

    portfolio_return = calculate_portfolio_return(weights, mean_returns)
    portfolio_risk = calculate_portfolio_risk(weights, covariance_matrix)
    print("\nInvestment Mix Results:")
    print("Weights:", weights)
    print("Expected Return:", portfolio_return)
    print("Risk:", portfolio_risk)


    # Check Risk Level
risk_level = check_risk_level(portfolio_risk)

print("\nRisk Analysis:")
print("Risk Level:", risk_level)

# Trigger Alert
send_alert(risk_level)



 
import pandas as pd
from investment_mix import (
    get_mix_by_risk,
    calculate_returns,
    calculate_portfolio_return,
    calculate_portfolio_risk
)

# Load crypto data
df = pd.read_csv("data/crypto_data1.csv")

# Step 1: Calculate returns
returns = calculate_returns(df)

# Step 2: Calculate statistics
mean_returns = returns.mean()
cov_matrix = returns.cov()

# Step 3: Choose risk level
risk_level = "medium"

# Step 4: Get rule-based weights
weights = get_mix_by_risk(risk_level)

# Step 5: Calculate portfolio performance
portfolio_return = calculate_portfolio_return(weights, mean_returns)
portfolio_risk = calculate_portfolio_risk(weights, cov_matrix)

# Step 6: Print Output
print("\nRisk Level:", risk_level)
print("Weights:", weights)
print("Expected Return:", portfolio_return)
print("Portfolio Risk:", portfolio_risk)





