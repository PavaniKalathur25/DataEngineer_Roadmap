# Batch Processing - File-based ETL

This repository demonstrates batch processing concepts:
- Collect data in **files (CSV)**
- Run ETL in **batches**
- Handle **latency** (daily/hourly jobs)
- Orchestrate using **Cron / Airflow**

## Structure
- `data/`: Raw and processed batch files
- `etl/`: Extract, Transform, Load scripts
- `scripts/batch_pipeline.py`: Orchestration for ETL
- `scheduler/cron_example.sh`: Example of cron-based scheduling
- `airflow_dag/batch_etl_dag.py`: Airflow DAG for scheduling

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run pipeline manually:
   ```bash
   python scripts/batch_pipeline.py

