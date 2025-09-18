from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark session
spark = SparkSession.builder.appName("IncrementalLoadCDC").getOrCreate()

# Load target (previous data)
target_df = spark.read.option("header", "true").csv("data/target_data.csv")

# Load new source data (Day 2)
source_df = spark.read.option("header", "true").csv("data/source_data_day2.csv")

# CDC Logic: Join and detect changes
# 1. Find updated or new records
merged_df = source_df.alias("s").join(
    target_df.alias("t"),
    on="id",
    how="outer"
).select(
    col("s.id").alias("id"),
    col("s.name").alias("name"),
    col("s.city").alias("city")
)

# Overwrite target with new changes (simulate MERGE)
merged_df.write.mode("overwrite").option("header", "true").csv("data/target_data.csv")

print("Incremental load complete. Target updated.")
