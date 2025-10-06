# 🤖 Service Principal Setup

A Service Principal acts like a "user identity" for apps or pipelines to access Azure securely.

## Why It’s Needed
When Databricks or Azure Data Factory needs to connect to ADLS or Synapse,
they can’t log in like humans — they use Service Principals.

## Steps (Using Azure CLI)

### Step 1: Create a Service Principal
```bash
az ad sp create-for-rbac \
  --name my-app-sp \
  --role "Storage Blob Data Contributor" \
  --scopes /subscriptions/<sub-id>/resourceGroups/<rg-name>
