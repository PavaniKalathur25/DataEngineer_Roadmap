---

### 📄 `polybase.md`
```markdown
# Synapse - PolyBase

**What is it?**  
- A feature in Synapse that lets you query **external data** stored in ADLS/Blob as if it were SQL tables.  

**Where it's actually used?**  
- Querying raw data from Data Lake before loading to warehouse.  
- Staging data during ETL processes.  

**Why used?**  
- Saves time by reading external files directly.  
- Reduces storage costs (no need to copy everything into Synapse first).  

**Any coding needed?**  
Yes, **T-SQL** for creating external tables and querying.  

**Sample Code**
```sql
-- Create External Data Source
CREATE EXTERNAL DATA SOURCE MyDataLake
WITH (
    TYPE = HADOOP,
    LOCATION = 'abfss://raw@storageaccount.dfs.core.windows.net/'
);

-- Create External File Format
CREATE EXTERNAL FILE FORMAT MyCsvFormat
WITH (
    FORMAT_TYPE = DELIMITEDTEXT,
    FORMAT_OPTIONS (FIELD_TERMINATOR = ',', STRING_DELIMITER = '"')
);

-- Create External Table
CREATE EXTERNAL TABLE dbo.SalesExternal (
    SaleID INT,
    ProductName VARCHAR(100),
    Amount DECIMAL(10,2)
)
WITH (
    LOCATION = '/sales/',
    DATA_SOURCE = MyDataLake,
    FILE_FORMAT = MyCsvFormat
);

-- Query External Table
SELECT TOP 10 * FROM dbo.SalesExternal;
