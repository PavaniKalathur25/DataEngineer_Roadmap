from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(
    "parallel_example",
    start_date=datetime(2025, 9, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    start = DummyOperator(task_id="start")

    task1 = DummyOperator(task_id="task1")
    task2 = DummyOperator(task_id="task2")
    task3 = DummyOperator(task_id="task3")

    end = DummyOperator(task_id="end")

    # Parallel execution (fan-out/fan-in pattern)
    start >> [task1, task2, task3] >> end
