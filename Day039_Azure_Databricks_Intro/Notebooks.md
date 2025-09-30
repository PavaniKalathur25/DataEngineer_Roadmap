# Databricks Notebooks

**What is it?**  
Interactive coding environment inside Databricks (like Jupyter but Spark-enabled).

**Where it's actually used?**
- Writing PySpark scripts for ETL.
- Running SQL queries on big data.
- Testing ML/AI experiments.

**Why used?**
- Combines code + output + visualization in one place.
- Supports multiple languages in one notebook (`%python`, `%sql`, `%scala`).

**Any coding needed?**
Yes. You write transformations, queries, and ML logic here.

**Sample SQL in Notebook**
```sql
%sql
SELECT region, COUNT(*) AS orders
FROM sales
GROUP BY region;
