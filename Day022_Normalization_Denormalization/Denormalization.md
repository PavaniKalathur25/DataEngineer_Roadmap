# Denormalization

## What is Denormalization?
- The opposite of normalization.
- Intentionally introduces redundancy to improve query performance.

**Keywords:** redundancy, OLAP, star schema, performance.

---

## Where it's used?
- Data Warehouses (Snowflake, BigQuery, Synapse, Redshift).
- BI dashboards, analytical queries.

---

## Why used?
- Speeds up read-heavy queries.
- Reduces complex joins.
- Improves performance for reporting & analytics.

---

## Any coding needed?
- SQL with denormalized schemas (Star Schema, Snowflake Schema).
- ETL/ELT processes (PySpark, ADF, Airflow).
