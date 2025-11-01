# Examples - Real Use Cases

## E-Commerce System Example

### Step 1: OLTP Layer
- Customer places order → Stored in Azure SQL Database.

### Step 2: Raw Storage
- Daily batch ingestion moves order data to Azure Data Lake (Raw Zone).

### Step 3: Processed Layer
- Azure Databricks cleans data → stores in Curated Zone (Parquet format).

### Step 4: Warehouse Layer
- Azure Synapse loads curated data into Fact & Dimension tables.

### Step 5: OLAP Layer
- Power BI dashboard reads data from Synapse for reporting.

---

## Example Data Flow (Simplified)

