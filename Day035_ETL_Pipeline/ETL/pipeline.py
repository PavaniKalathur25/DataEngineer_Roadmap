from extract import extract
from transform import transform
from load import load

def main():
    data = extract("../data/employees.csv")
    clean_data = transform(data)
    load(clean_data)
    print("ETL Pipeline Completed ✅")

if __name__ == "__main__":
    main()
