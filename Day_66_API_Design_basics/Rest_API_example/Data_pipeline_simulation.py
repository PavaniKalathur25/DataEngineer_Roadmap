def process_data(data):
    # Simulate data cleaning & transformation
    data["cleaned"] = True
    data["message"] = f"Data for {data.get('source', 'unknown')} processed successfully."
    return data
