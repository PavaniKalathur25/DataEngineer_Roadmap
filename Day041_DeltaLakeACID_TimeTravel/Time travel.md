---

### 📄 `time_travel.md`
```markdown
# Delta Lake - Time Travel

**What is it?**  
- Ability to query old versions of data stored in Delta Lake.  
- Acts like a "time machine" for your data.

**Where it's actually used?**  
- Debugging pipeline errors by checking old versions.  
- Auditing and compliance to verify historical data.  
- Restoring data accidentally deleted/overwritten.  

**Why used?**  
- Keeps history of data changes.  
- Helps in rollback and recovery.  

**Any coding needed?**  
Yes, Delta Lake APIs provide version/timestamp-based reads.

**Sample Code**
```python
# Read older version by version number
df_v1 = spark.read.format("delta").option("versionAsOf", 1).load("/mnt/raw/delta_sales")

# Read older version by timestamp
df_old = spark.read.format("delta").option("timestampAsOf", "2025-09-25").load("/mnt/raw/delta_sales")

# Rollback table to old version
from delta.tables import DeltaTable
deltaTable = DeltaTable.forPath(spark, "/mnt/raw/delta_sales")
deltaTable.restoreToVersion(1)
