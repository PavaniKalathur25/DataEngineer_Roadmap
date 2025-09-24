from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, TimestampType

# Spark session
spark = SparkSession.builder.appName("KafkaStreamingExample").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Define schema for incoming JSON
schema = StructType() \
    .add("user", StringType()) \
    .add("action", StringType()) \
    .add("timestamp", StringType())

# Read from Kafka topic
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "realtime_events") \
    .load()

# Convert Kafka value (binary) into JSON fields
events_df = df.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.*")

# Simple transformation: count actions per user
agg_df = events_df.groupBy("user", "action").count()

# Write results to console (real-time output)
query = agg_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
