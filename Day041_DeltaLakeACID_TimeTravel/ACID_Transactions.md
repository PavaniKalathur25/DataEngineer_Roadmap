# Delta Lake - ACID Transactions

**What is it?**  
- Delta Lake adds **ACID (Atomicity, Consistency, Isolation, Durability)** guarantees on top of a Data Lake.

**Where it's actually used?**  
- Batch & Streaming pipelines writing to the same table.  
- Preventing corrupt data when multiple jobs/users update data.  

**Why used?**  
- Ensures data reliability and consistency.  
- Supports concurrent reads/writes safely.  

**Any coding needed?**  
Yes, PySpark code to write/read Delta tables.

**Sample Code**
```python
# Write data with ACID guarantees
data = [("A", 100), ("B", 200)]
df = spark.createDataFrame(data, ["Customer", "Amount"])

df.write.format("delta").mode("overwrite").save("/mnt/raw/delta_sales")

# Read data back
df = spark.read.format("delta").load("/mnt/raw/delta_sales")
df.show()
