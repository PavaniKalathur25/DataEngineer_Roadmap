import os
import pandas as pd
from etl.extract import extract
from etl.transform import transform
from etl.load import load

def main():
    data_dir = "data/"
    target_file = os.path.join(data_dir, "processed_sales.csv")

    # Create target file with header if not exists
    if not os.path.exists(target_file):
        pd.DataFrame(columns=["order_id","product","amount","tax","total_amount"]).to_csv(target_file, index=False)

    # Process each batch file
    for file in os.listdir(data_dir):
        if file.startswith("batch") and file.endswith(".csv"):
            file_path = os.path.join(data_dir, file)
            df = extract(file_path)
            df = transform(df)
            load(df, target_file)

if __name__ == "__main__":
    main()
