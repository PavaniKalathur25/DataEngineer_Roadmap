# Orchestration Basics (Airflow, Prefect, ADF)

This repo contains examples of orchestration tools used in Data Engineering:
- **Airflow** → Python-based DAGs for ETL orchestration.
- **Prefect** → Modern Python-first orchestration tool.
- **Azure Data Factory (ADF)** → Cloud-native orchestration, JSON export of pipelines.

## Why Orchestration?
- Automates workflows (ETL/ELT pipelines).
- Manages dependencies between tasks.
- Monitors success/failure of jobs.
- Supports scheduling & event-driven pipelines.

## Structure
- `airflow_dag/etl_airflow_dag.py` → Example Airflow DAG for ETL.
- `prefect_flow/etl_prefect_flow.py` → Prefect flow example.
- `adf_pipeline/sample_pipeline.json` → Sample ADF pipeline export.
- `requirements.txt` → Python dependencies.

## How to Run
### Airflow
1. Install Airflow (local or docker-compose).
2. Copy DAG into Airflow DAGs folder.
3. Run Airflow UI & trigger DAG.

### Prefect
```bash
pip install prefect
python prefect_flow/etl_prefect_flow.py
