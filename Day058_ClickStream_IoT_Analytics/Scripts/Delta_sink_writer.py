from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col

spark = SparkSession.builder \
    .appName("DeltaSinkWriter") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

schema = "deviceId STRING, eventType STRING, value DOUBLE, timestamp STRING"

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "clickstream_topic") \
    .load()

parsed_df = df.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.*")

# Write to Delta table
query = parsed_df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "checkpoint/day58_cp") \
    .option("path", "delta/clickstream_data") \
    .trigger(processingTime="15 seconds") \
    .start()

query.awaitTermination()
