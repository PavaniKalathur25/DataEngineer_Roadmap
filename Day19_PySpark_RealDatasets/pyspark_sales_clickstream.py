from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# -------------------------
# 1. Start SparkSession
# -------------------------
spark = SparkSession.builder \
    .appName("Day19_PySpark_RealDatasets") \
    .getOrCreate()

print("✅ SparkSession started!")

# -------------------------
# 2. Load Sales Data
# -------------------------
sales = spark.read.option("header", "true").option("inferSchema", "true").csv("data/sales.csv")
print("\n👉 Sales Data:")
sales.show(5)

# Total revenue by product
print("\n👉 Total Revenue by Product:")
sales.groupBy("product_id") \
     .agg(F.sum("amount").alias("total_revenue")) \
     .orderBy(F.desc("total_revenue")) \
     .show()

# Daily sales trend
print("\n👉 Daily Sales Trend:")
sales.groupBy("date") \
     .agg(F.sum("amount").alias("daily_revenue")) \
     .orderBy("date") \
     .show()

# -------------------------
# 3. Load Clickstream Data
# -------------------------
clicks = spark.read.option("header", "true").option("inferSchema", "true").csv("data/clickstream.csv")
print("\n👉 Clickstream Data:")
clicks.show(5)

# Total clicks per user
print("\n👉 Total Clicks per User:")
clicks.groupBy("user_id") \
      .agg(F.count("page_url").alias("total_clicks")) \
      .orderBy(F.desc("total_clicks")) \
      .show()

# Rank pages visited per user
print("\n👉 Rank pages visited per user:")
window = Window.partitionBy("user_id").orderBy(F.asc("timestamp"))
clicks.withColumn("row_num", F.row_number().over(window)) \
      .show(10)

# -------------------------
# 4. Stop Spark
# -------------------------
spark.stop()
print("✅ SparkSession stopped!")
