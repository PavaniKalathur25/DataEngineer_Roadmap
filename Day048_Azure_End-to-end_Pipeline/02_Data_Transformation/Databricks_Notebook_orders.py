from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

spark = SparkSession.builder.appName("EcommerceDataTransform").getOrCreate()

# Read raw orders from ADLS
raw_path = "abfss://raw@ecommercedatalake.dfs.core.windows.net/orders.csv"
df = spark.read.option("header", True).csv(raw_path)

# Filter only completed orders
df_clean = df.filter(col("status") == "completed")

# Aggregate total sales by region
df_agg = df_clean.groupBy("region").agg(_sum(col("amount")).alias("total_sales"))

# Write result to processed zone
processed_path = "abfss://processed@ecommercedatalake.dfs.core.windows.net/sales_by_region"
df_agg.write.mode("overwrite").parquet(processed_path)

print("✅ Data transformation completed successfully.")
