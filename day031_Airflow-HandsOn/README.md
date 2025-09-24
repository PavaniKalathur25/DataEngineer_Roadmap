# Airflow Hands-on (DAGs, Tasks, Scheduling)

This repo demonstrates basics of Apache Airflow:
- DAG creation
- Defining tasks
- Scheduling with cron / presets
- Setting dependencies between tasks

## Why Airflow?
- Automates ETL/ELT pipelines
- Manages task dependencies
- Provides monitoring & alerting
- Scales to complex workflows

## Structure
- `dags/etl_daily_dag.py`: Example DAG with extract → transform → load tasks.
- `requirements.txt`: Python dependencies.

## How to Run
1. Install Airflow (via pip or docker-compose).
   ```bash
   pip install apache-airflow
