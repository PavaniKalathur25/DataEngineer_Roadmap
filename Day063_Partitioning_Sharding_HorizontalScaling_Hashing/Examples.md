# Examples — Real-world Applications

## Example 1: Azure Data Lake + Databricks
**Flow:**
Raw data → Partitioned by `region` and `year` → Processed in parallel using Spark.

**Benefit:** Faster read performance, less memory use.

---

## Example 2: Cosmos DB (Sharded)
User data is sharded by `user_id`:
- Shard 1: user_id 1–1M
- Shard 2: user_id 1M–2M

**Benefit:** Queries hit only the needed shard.

---

## Example 3: Kafka
Messages distributed to partitions based on a key:
```python
partition = hash(user_id) % num_partitions
