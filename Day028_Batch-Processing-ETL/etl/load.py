def load(df, file_path):
    print(f"Loading processed data to {file_path}")
    df.to_csv(file_path, mode='a', index=False, header=False)
    print("Data loaded successfully.")
