def generate_report(return_value, risk_value, risk_level):
    report = f"""
    ===== Portfolio Report =====
    Expected Return : {return_value}
    Risk Value      : {risk_value}
    Risk Level      : {risk_level}
    ============================
    """
    return report

def save_report(report, filename="reports/portfolio_report.txt"):
    with open(filename, "w") as file:
        file.write(report)