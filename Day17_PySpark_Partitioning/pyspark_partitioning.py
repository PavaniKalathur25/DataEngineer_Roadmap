from pyspark.sql import SparkSession

# -------------------------
# 1. Start SparkSession
# -------------------------
spark = SparkSession.builder \
    .appName("Day17_PySpark_Partitioning") \
    .config("spark.sql.shuffle.partitions", "4") \
    .enableHiveSupport() \  # Needed for bucketing example
    .getOrCreate()

print("✅ SparkSession started!")

# -------------------------
# 2. Load Sample Data
# -------------------------
employees = spark.read.option("header", "true").option("inferSchema", "true").csv("data/employees.csv")

print("Employees Data:")
employees.show()

print("👉 Current partitions:", employees.rdd.getNumPartitions())

# -------------------------
# 3. Repartition (with shuffle)
# -------------------------
print("👉 Repartition to 6 partitions (balanced shuffle):")
repart_df = employees.repartition(6, "department")
print("Partitions after repartition:", repart_df.rdd.getNumPartitions())

# -------------------------
# 4. Coalesce (without shuffle)
# -------------------------
print("👉 Coalesce to 2 partitions (merge only):")
coalesce_df = employees.coalesce(2)
print("Partitions after coalesce:", coalesce_df.rdd.getNumPartitions())

# -------------------------
# 5. Bucketing (write as bucketed table)
# -------------------------
print("👉 Writing data into 4 buckets by department...")
employees.write.bucketBy(4, "department").sortBy("salary").saveAsTable("bucketed_employees")

print("✅ Bucketed table 'bucketed_employees' created.")

# -------------------------
# 6. Stop Spark
# -------------------------
spark.stop()
print("✅ SparkSession stopped!")
