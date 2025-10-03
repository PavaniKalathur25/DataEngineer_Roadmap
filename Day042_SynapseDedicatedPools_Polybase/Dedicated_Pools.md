# Synapse - Dedicated SQL Pools

**What is it?**  
- A **provisioned data warehouse** in Azure Synapse Analytics.  
- Uses **Massively Parallel Processing (MPP)** to handle very large datasets.

**Where it's actually used?**  
- Enterprise Data Warehousing.  
- Running analytics queries on billions of rows.  
- Power BI dashboards and advanced BI reporting.  

**Why used?**  
- Fast query performance at scale.  
- Handles complex joins, aggregations, and reporting workloads.  

**Any coding needed?**  
Yes, queries are written in **T-SQL**.  

**Sample Query**
```sql
-- Example: Create a fact table
CREATE TABLE FactSales (
    SaleID INT,
    ProductID INT,
    CustomerID INT,
    Amount DECIMAL(10,2),
    SaleDate DATE
)
WITH (DISTRIBUTION = HASH(ProductID), CLUSTERED COLUMNSTORE INDEX);
