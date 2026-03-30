def check_risk_level(risk_value):
    if risk_value < 0.02:
        return "Low Risk"
    elif risk_value < 0.05:
        return "Medium Risk"
    else:
        return "High Risk"