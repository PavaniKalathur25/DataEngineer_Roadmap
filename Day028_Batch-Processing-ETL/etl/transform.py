def transform(df):
    print("Transforming data...")
    # Example: Add tax column
    df['tax'] = df['amount'] * 0.1
    df['total_amount'] = df['amount'] + df['tax']
    return df
