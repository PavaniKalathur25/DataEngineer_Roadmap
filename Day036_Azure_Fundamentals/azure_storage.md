# Azure Storage Basics

**What is it?**  
Azure Storage is where you keep your data (files, tables, messages, backups).

**Where it's actually used?**
- Store raw data from different sources (logs, files, JSON, CSV).
- Data Lake for analytics pipelines (PySpark, Synapse, Databricks).
- Backup/archive of data.

**Why used (any coding needed)?**
- Reliable, secure, cheap compared to physical storage.
- Used heavily in Data Engineering pipelines.
- You’ll need coding if connecting via SDKs (Python, PySpark) or scripts.

**Sample PySpark Code**
```python
spark.read.format("parquet").load("abfss://container@storage.dfs.core.windows.net/data")
