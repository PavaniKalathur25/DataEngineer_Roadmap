from sqlalchemy import create_engine

def load(df, db_path="../employees.db"):
    print("Loading data into SQLite...")
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql("employees", engine, if_exists="replace", index=False)
    print("✅ Load complete.")
