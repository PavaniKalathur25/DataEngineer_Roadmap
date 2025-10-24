# Serverless SQL Pools in Azure Synapse

## What is it?
A **pay-per-query SQL engine** to analyze files (CSV, Parquet, JSON) in Azure Data Lake.

## Where used?
- Ad-hoc exploration of raw data.
- Quick queries on logs, clickstreams.
- Pre-validation before ETL.

## Why used?
- No infrastructure management.
- Cost-effective (pay only for queries).
- Instant data exploration.

## Coding Needed?
- SQL only.

### Example
```sql
SELECT TOP 10 *
FROM OPENROWSET(
    BULK 'https://yourstorage.dfs.core.windows.net/container/sales/*.csv',
    FORMAT = 'CSV',
    FIRSTROW = 2
) AS salesData;
