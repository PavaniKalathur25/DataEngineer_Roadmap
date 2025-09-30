# Azure Blob Storage

**What is it?**  
Blob = Binary Large Object. Azure Blob Storage is a cloud-based object storage for unstructured data (images, videos, JSON, CSV, logs, backups).

**Where it's actually used?**
- Store raw data coming from different sources (IoT, logs, API outputs).
- Staging area before transformation (ADF, Databricks, PySpark jobs).
- Backup files, media files, archives.

**Why used?**
- Cheap and scalable storage.
- Can store huge datasets (petabytes).
- Access anywhere with REST API.
- Different pricing tiers (Hot, Cool, Archive).

**Any coding needed?**
Yes, if you’re accessing via SDKs or PySpark.

**Sample PySpark Code**
```python
# Reading data from Blob storage
spark.read.text("wasbs://container@storageaccount.blob.core.windows.net/rawdata/")
