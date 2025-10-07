# Create Log Analytics Workspace
az monitor log-analytics workspace create \
  --resource-group my-rg \
  --workspace-name my-laworkspace \
  --location eastus

# List workspaces
az monitor log-analytics workspace list -o table

# Link Data Factory to Log Analytics
az resource update \
  --ids $(az resource show \
  --resource-group my-rg \
  --name my-adf \
  --resource-type "Microsoft.DataFactory/factories" \
  --query id -o tsv) \
  --set properties.diagnostics.logAnalytics.workspaceId="/subscriptions/<sub-id>/resourcegroups/my-rg/providers/microsoft.operationalinsights/workspaces/my-laworkspace"

# Create metric alert (example)
az monitor metrics alert create \
  --name "HighCPUAlert" \
  --resource-group my-rg \
  --scopes /subscriptions/<sub-id>/resourceGroups/my-rg/providers/Microsoft.Compute/virtualMachines/myVM \
  --condition "avg Percentage CPU > 80" \
  --description "Alert when CPU > 80%"
