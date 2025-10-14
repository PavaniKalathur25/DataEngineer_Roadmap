# Day 52 - Spark Structured Streaming: WriteStream Example
# Example: Reading from Kafka and writing to console
# Ensure Kafka is running and topic 'orders' exists

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WriteStreamExample").getOrCreate()

# 1️⃣ Read live data from Kafka topic
kafka_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "orders")
    .load()
)

# 2️⃣ Convert binary to string
orders_df = kafka_df.selectExpr("CAST(value AS STRING) as order_data")

# 3️⃣ Write output to console in real time
query = (
    orders_df.writeStream
    .outputMode("append")
    .format("console")
    .option("truncate", "false")
    .start()
)

query.awaitTermination()
