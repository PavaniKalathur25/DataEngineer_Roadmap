from prefect import flow, task

@task
def extract():
    print("Extracting data...")

@task
def transform():
    print("Transforming data...")

@task
def load():
    print("Loading data into warehouse...")

@flow
def etl_flow():
    data = extract()
    transformed = transform()
    load()

if __name__ == "__main__":
    etl_flow()
