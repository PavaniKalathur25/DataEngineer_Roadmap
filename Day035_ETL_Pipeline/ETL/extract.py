import pandas as pd

def extract(path):
    print("Extracting data...")
    return pd.read_csv(path)
