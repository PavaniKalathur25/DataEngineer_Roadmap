from extract.extract_data import extract
from transform.transform_data import transform
from load.load_data import load

def main():
    source_file = 'data/source_data.csv'
    target_file = 'data/transformed_data.csv'
    
    # ETL process
    data = extract(source_file)
    data = transform(data)
    load(data, target_file)

if __name__ == "__main__":
    main()
