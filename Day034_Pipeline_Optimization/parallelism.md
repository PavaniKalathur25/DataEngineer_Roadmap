# Parallelism in Pipelines

## What is it?
Running multiple pipeline tasks simultaneously.

## Where it's used?
- Loading multiple tables/files.
- Running independent ETL transformations.
- Streaming jobs with partitions.

## Why used?
- Saves time (faster execution).
- Improves throughput.
- Better resource utilization.

## Coding Needed?
- Configurations in Airflow, ADF, Databricks.
- Spark: `repartition()`, `parallelize()`.

## Keywords
- Concurrency, Scalability, Throughput, Partitioning
