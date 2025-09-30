
---

### 📄 `data_lake_gen2.md`
```markdown
# Azure Data Lake Storage Gen2

**What is it?**  
Data Lake Gen2 = Blob Storage + Hierarchical Namespace.  
It allows folder-like structure with directories & subdirectories (like a real file system).  
Optimized for big data analytics (ETL, ML, AI).

**Where it's actually used?**
- As the main Data Lake for enterprise analytics.
- Store structured (Parquet, CSV) + unstructured (images, logs) + semi-structured (JSON, Avro).
- Feeding Azure Databricks, Synapse, HDInsight, Spark pipelines.

**Why used?**
- Handles big data with security, performance, and analytics support.
- Integrates with Hadoop/Spark ecosystem.
- Better access control (ACLs, RBAC).

**Any coding needed?**
Yes, usually with PySpark or Python SDK.

**Sample PySpark Code**
```python
# Reading parquet from Data Lake Gen2
spark.read.format("parquet").load("abfss://datalake@storageaccount.dfs.core.windows.net/processed/")
