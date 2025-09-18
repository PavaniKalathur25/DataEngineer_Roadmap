# Incremental Loads, CDC, and Merge Statements

This repo demonstrates:
- Incremental Loads (loading only new/updated records)
- CDC (Change Data Capture)
- MERGE statement in SQL
- PySpark incremental pipeline

## Structure
- `data/`: Sample CSVs simulating daily source data.
- `sql/merge_example.sql`: Example of SQL MERGE (UPSERT).
- `pyspark/incremental_pipeline.py`: PySpark incremental load example.
- `requirements.txt`: Python dependencies.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run PySpark pipeline:
   ```bash
   spark-submit pyspark/incremental_pipeline.py
