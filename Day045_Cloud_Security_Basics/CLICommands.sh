---

#### ⚙️ `cli_commands.sh`
```bash
# Create Service Principal
az ad sp create-for-rbac --name my-app-sp --role "Storage Blob Data Contributor" --scopes /subscriptions/<sub-id>/resourceGroups/<rg-name>

# List Role Assignments
az role assignment list --assignee <appId>

# Create Key Vault
az keyvault create --name my-keyvault --resource-group my-rg --location eastus

# Add Secret to Key Vault
az keyvault secret set --vault-name my-keyvault --name "sp-secret" --value "xxxx"
