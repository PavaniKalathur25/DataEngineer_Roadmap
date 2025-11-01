# Notes — Partitioning, Sharding, Horizontal Scaling & Hashing

## 1️⃣ Partitioning
**Definition:** Splitting a large table or dataset into smaller logical pieces (based on column values like `date`, `region`, or `category`).

**Where Used:**
- Spark, Hive, Delta Lake, Synapse
- Azure Data Lake folder structures

**Why Used:**
- Faster queries (partition pruning)
- Parallel data reads/writes
- Better organization

**Example:**
```python
df.write.partitionBy("year", "region").parquet("abfss://sales@datalake.dfs.core.windows.net/partitioned/")
