# Mounting ADLS in Databricks

**What is it?**  
- Mounting = making an ADLS container look like a local folder in Databricks.  
- Example: `/mnt/datalake/raw` → directly points to your ADLS path.  

**Where it's actually used?**
- Simplifies reading/writing files from ADLS without writing long URLs.
- Used in pipelines where multiple notebooks/jobs need the same data source.

**Why used?**
- Easy access → no need to retype SAS tokens or account names each time.
- Reusability → same mounted path can be reused across projects.

**Any coding needed?**
Yes, Databricks provides utilities (`dbutils.fs.mount`).

**Sample Code**
```python
configs = {
  "fs.azure.account.auth.type": "OAuth",
  "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
  "fs.azure.account.oauth2.client.id": "<app-id>",
  "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="kv-scope", key="app-secret"),
  "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<tenant-id>/oauth2/token"
}

dbutils.fs.mount(
  source = "abfss://raw@storageaccount.dfs.core.windows.net/",
  mount_point = "/mnt/raw",
  extra_configs = configs
)
