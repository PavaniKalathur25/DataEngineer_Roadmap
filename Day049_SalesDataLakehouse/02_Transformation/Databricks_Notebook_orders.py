# Databricks PySpark Script — Sales Lakehouse (Bronze → Silver → Gold)
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, to_timestamp

spark = SparkSession.builder.appName("SalesLakehouse").getOrCreate()

# Paths (replace with your actual ADLS URLs)
bronze_path = "abfss://bronze@saleslakehouse.dfs.core.windows.net/orders_sample.csv"
silver_path = "abfss://silver@saleslakehouse.dfs.core.windows.net/sales_cleaned_delta"
gold_path   = "abfss://gold@saleslakehouse.dfs.core.windows.net/sales_summary_delta"

# Read raw CSV
df = spark.read.option("header", True).csv(bronze_path)

# Clean and filter
df_clean = (df.withColumn("amount", col("amount").cast("double"))
              .withColumn("order_ts", to_timestamp(col("order_ts")))
              .filter(col("status") == "completed"))

# Write Silver layer
df_clean.write.format("delta").mode("overwrite").save(silver_path)

# Aggregate for Gold layer
df_summary = df_clean.groupBy("region").agg(_sum("amount").alias("total_sales"))
df_summary.write.format("delta").mode("overwrite").save(gold_path)

print("✅ Data successfully written to Silver and Gold Delta tables.")
