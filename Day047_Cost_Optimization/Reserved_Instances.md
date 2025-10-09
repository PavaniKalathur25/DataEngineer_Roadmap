# 🧮 Reserved Instances (RI)

## What is it?
Reserved Instances (RIs) are a way to **prepay** for Azure compute resources (like VMs, Synapse pools, or Databricks clusters)
for **1 or 3 years** in exchange for up to **72% discount**.

## Where Used
- Long-running Databricks clusters  
- Always-on Synapse Dedicated SQL pools  
- Persistent ETL pipelines in Azure Data Factory  

## Why Used
- Reduces compute cost for predictable workloads  
- Locks pricing for long-term stability  
- Ideal for production jobs that run continuously

## Example CLI
```bash
az vm list-skus --location eastus --size Standard_D4s_v3
# Check eligible instances for reservation

az reservation-order calculate \
  --sku-name Standard_D4s_v3 \
  --term P1Y \
  --billing-scope "/subscriptions/<sub-id>"
