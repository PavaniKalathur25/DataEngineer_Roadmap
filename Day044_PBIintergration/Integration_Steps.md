# Integrating Power BI with Azure Synapse / Data Lake

## 1. Connect Power BI to Azure Synapse
1. Open Power BI Desktop → "Get Data".
2. Select **Azure Synapse Analytics (SQL Data Warehouse)**.
3. Enter workspace & server details.
4. Sign in using your Azure credentials.
5. Select tables/views → Load into Power BI.

## 2. Connect Power BI to Azure Data Lake (via Dataflows)
1. In Power BI Service → "Dataflows" → "Add new entities".
2. Choose **Azure Data Lake Storage Gen2** connector.
3. Enter storage account URL.
4. Map columns, transform data if needed.
5. Save & schedule refresh.

## 3. Real-time Dashboard Integration
- Use **streaming datasets** or connect Event Hub → Stream Analytics → Power BI output.
- Dashboards update in near real-time as new events arrive.

## 4. Publish & Share
1. Click **Publish** in Power BI Desktop → select workspace.
2. Create dashboard → Pin visuals.
3. Set refresh schedule or enable live connection.

**Tip:** Always ensure datasets in Synapse or Data Lake are optimized with partitions and indexes before connecting.
