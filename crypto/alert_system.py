def send_alert(risk_level):
    print("\n===== ALERT SYSTEM =====")

    if risk_level == "High Risk":
        print(" WARNING: PORTFOLIO RISK IS HIGH! ")
    elif risk_level == "Medium Risk":
        print(" Portfolio risk is MEDIUM.")
    else:
        print(" Portfolio risk is LOW.")

    print("========================\n")