
---

## 📄 **airflow_dag/etl_airflow_dag.py**

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Example ETL functions
def extract():
    print("Extracting data...")

def transform():
    print("Transforming data...")

def load():
    print("Loading data into warehouse...")

# Define DAG
default_args = {
    'owner': 'data_engineer',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id="etl_airflow_dag",
    default_args=default_args,
    start_date=datetime(2025, 9, 18),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=load
    )

    # DAG dependencies
    extract_task >> transform_task >> load_task
