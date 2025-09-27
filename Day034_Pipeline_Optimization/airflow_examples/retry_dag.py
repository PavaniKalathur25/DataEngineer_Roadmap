from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(
    "retry_example",
    start_date=datetime(2025, 9, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    flaky_task = BashOperator(
        task_id="unstable_api_call",
        bash_command="exit 1",  # simulate failure
        retries=3,              # retry 3 times
        retry_delay=timedelta(minutes=2)  # wait 2 min before retry
    )
