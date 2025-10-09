# 🧠 Python SDK Examples for Cost Optimization

## Change Storage Tier Programmatically
```python
from azure.storage.blob import BlobClient

blob = BlobClient.from_connection_string(
    conn_str="DefaultEndpointsProtocol=https;AccountName=mystorage;AccountKey=xxxx;",
    container_name="reports",
    blob_name="2023_data.csv"
)
blob.set_standard_blob_tier("Cool")
