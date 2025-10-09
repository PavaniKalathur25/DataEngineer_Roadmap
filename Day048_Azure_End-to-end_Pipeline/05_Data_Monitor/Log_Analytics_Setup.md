# 📈 Log Analytics Setup

1️⃣ Go to **Azure Portal → Log Analytics Workspaces**  
2️⃣ Create a workspace and link it to:
   - Azure Data Factory
   - Azure Databricks
   - Synapse Analytics

3️⃣ Enable **Diagnostic Settings** for each service to send logs to this workspace.

4️⃣ Use KQL queries (see `azure_monitor_queries.kql`) to monitor:
   - Failed pipeline runs
   - Databricks job errors
   - Data load durations
   - Synapse query costs
