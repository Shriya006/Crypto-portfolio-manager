import pandas as pd

def load_crypto_data(file_path):
    df = pd.read_csv(file_path)
    df.set_index("Date", inplace=True)
    return df

def calculate_returns(df):
    returns = df.pct_change().dropna()
    return returns