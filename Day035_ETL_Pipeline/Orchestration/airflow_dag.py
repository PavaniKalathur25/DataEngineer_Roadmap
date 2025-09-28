from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Import your ETL scripts
sys.path.append(os.path.abspath("../etl"))
from extract import extract
from transform import transform
from load import load

default_args = {
    "owner": "airflow",
    "retries": 2,
    "retry_delay": timedelta(minutes=2)
}

def run_extract():
    return extract("../data/employees.csv")

def run_transform():
    import pandas as pd
    df = extract("../data/employees.csv")
    clean = transform(df)
    clean.to_csv("../data/clean_employees.csv", index=False)

def run_load():
    import pandas as pd
    df = pd.read_csv("../data/clean_employees.csv")
    load(df)

with DAG(
    dag_id="etl_pipeline_dag",
    default_args=default_args,
    description="ETL Pipeline with Airflow",
    schedule_interval="@daily",
    start_date=datetime(2025, 9, 27),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=run_extract
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=run_transform
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=run_load
    )

    extract_task >> transform_task >> load_task
