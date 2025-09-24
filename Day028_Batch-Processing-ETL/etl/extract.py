import pandas as pd

def extract(file_path):
    print(f"Extracting data from {file_path}")
    return pd.read_csv(file_path)
