def transform(data):
    print("Transforming data...")
    # Fill missing age with average
    data['age'] = data['age'].fillna(data['age'].mean().round())
    # Fill missing salary with average
    data['salary'] = data['salary'].fillna(data['salary'].mean().round())
    return data
