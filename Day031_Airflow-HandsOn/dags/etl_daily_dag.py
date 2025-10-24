
---

## 📄 **dags/etl_daily_dag.py**

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Step 1: Define ETL functions
def extract():
    print("Extracting data from source...")

def transform():
    print("Transforming data...")

def load():
    print("Loading data into warehouse...")

# Step 2: Define DAG arguments
default_args = {
    "owner": "data_engineer",
    "retries": 2,
    "retry_delay": timedelta(minutes=3)
}

# Step 3: Create DAG
with DAG(
    dag_id="etl_daily_dag",
    default_args=default_args,
    description="Daily ETL pipeline DAG",
    start_date=datetime(2025, 9, 17),
    schedule_interval="@daily",   # can also use cron: "0 9 * * *"
    catchup=False
) as dag:

    # Step 4: Define tasks
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

    # Step 5: Set dependencies
    extract_task >> transform_task >> load_task
