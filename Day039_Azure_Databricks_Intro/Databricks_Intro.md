# Azure Databricks - Introduction

**What is it?**  
A cloud-based data engineering and machine learning platform built on Apache Spark.  
Provides an environment to process big data, run analytics, and build AI models.

**Where it's actually used?**
- Ingest, transform, and process large datasets.
- Build ETL pipelines (batch & streaming).
- Train and deploy ML/AI models.

**Why used?**
- Scalable: handles TBs–PBs of data.
- Integrates with Azure Data Lake, Synapse, ADF, Power BI.
- Supports multiple languages (PySpark, SQL, Python, R, Scala).

**Any coding needed?**
Yes, mainly PySpark, SQL, Python.

**Sample PySpark Code**
```python
df = spark.read.csv("/mnt/datalake/raw/sales.csv", header=True)
df.groupBy("region").sum("amount").show()
