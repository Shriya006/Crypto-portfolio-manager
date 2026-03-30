
import numpy as np

def calculate_portfolio_return(weights, mean_returns):
    portfolio_return = np.dot(weights, mean_returns)
    return portfolio_return

def calculate_portfolio_risk(weights, covariance_matrix):
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))
    return portfolio_risk

def generate_equal_weights(n):
    return np.array([1/n] * n)


# investment_mix.py

def get_mix_by_risk(risk_level):
    """
    Returns allocation % based on risk level
    """

    risk_level = risk_level.lower()

    if risk_level == "low":
        return {
            "Stable Assets": 0.70,
            "Medium Assets": 0.20,
            "High Risk Assets": 0.10
        }

    elif risk_level == "medium":
        return {
            "Stable Assets": 0.40,
            "Medium Assets": 0.40,
            "High Risk Assets": 0.20
        }

    elif risk_level == "high":
        return {
            "Stable Assets": 0.20,
            "Medium Assets": 0.30,
            "High Risk Assets": 0.50
        }

    else:
        raise ValueError("Invalid risk level. Choose: low, medium, high")


