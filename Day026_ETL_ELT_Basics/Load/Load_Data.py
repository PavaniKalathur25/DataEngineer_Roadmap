def load(data, file_path):
    print("Loading data to", file_path)
    data.to_csv(file_path, index=False)
    print("Data loaded successfully.")
