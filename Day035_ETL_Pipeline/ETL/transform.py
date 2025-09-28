def transform(df):
    print("Transforming data...")
    df["salary"] = df["salary"].fillna(0).astype(int)
    df["department"] = df["department"].str.upper()
    return df
