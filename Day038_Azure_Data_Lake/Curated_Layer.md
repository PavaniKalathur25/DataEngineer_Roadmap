# Curated Layer (Silver)

**What is it?**  
The cleaned and transformed layer. Data is standardized, validated, and often stored in efficient formats (Parquet, Delta).

**Where it's actually used?**
- Prepares data for downstream analytics.
- Used by data engineers to build fact and dimension tables.

**Why used?**
- Reduces complexity for analysts and scientists.
- Improves performance (compressed & optimized formats).

**Any coding needed?**
Yes: PySpark or SQL transformations.

**Sample PySpark Code**
```python
df = spark.read.csv("abfss://datalake@storageaccount.dfs.core.windows.net/raw/sales/")
clean_df = df.filter(df["amount"] > 0).dropDuplicates()
clean_df.write.format("parquet").mode("overwrite").save("abfss://datalake@storageaccount.dfs.core.windows.net/curated/sales/")
