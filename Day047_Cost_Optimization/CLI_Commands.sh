---

#### ⚙️ `cli_commands.sh`
```bash
# List reserved instance recommendations
az advisor recommendation list --category Cost

# Set blob storage tier
az storage blob set-tier \
  --account-name mystorage \
  --container-name logs \
  --name old_pipeline_logs.csv \
  --tier Archive

# Apply lifecycle management policy
az storage account management-policy create \
  --account-name mystorage \
  --policy @policy.json
