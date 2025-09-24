from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
from etl.extract import extract
from etl.transform import transform
from etl.load import load

def run_batch_etl():
    data_dir = "data/"
    target_file = os.path.join(data_dir, "processed_sales.csv")
    for file in os.listdir(data_dir):
        if file.startswith("batch") and file.endswith(".csv"):
            df = extract(os.path.join(data_dir, file))
            df = transform(df)
            load(df, target_file)

with DAG(
    dag_id="batch_etl_dag",
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:
    task1 = PythonOperator(
        task_id="run_batch_etl",
        python_callable=run_batch_etl
    )
