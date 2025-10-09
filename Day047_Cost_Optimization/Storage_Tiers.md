---

#### 📘 `storage_tiers.md`
```markdown
# 🗃️ Azure Storage Tiers

## What is it?
Azure Blob and Data Lake storage offer **Hot**, **Cool**, and **Archive** tiers to balance cost and data access frequency.

## Where Used
- Data Lake zones (raw, curated, archived)  
- Long-term backup of pipeline logs or processed data  

## Why Used
- Save cost by aligning data storage with usage patterns  
- Automate data movement across tiers (via Lifecycle Policies)

## Example CLI
```bash
# Move file to Cool Tier
az storage blob set-tier \
  --account-name mystorage \
  --container-name reports \
  --name 2024_data.csv \
  --tier Cool
