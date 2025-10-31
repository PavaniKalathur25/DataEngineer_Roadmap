#!/usr/bin/env python3
# scripts/spark_consumer.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

# ---------- Spark session ----------
spark = SparkSession.builder \
    .appName("ClickstreamStreaming") \
    .config("spark.sql.shuffle.partitions", 8) \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# ---------- Schema for incoming JSON ----------
schema = StructType([
    StructField("userId", StringType(), True),
    StructField("page", StringType(), True),
    StructField("action", StringType(), True),
    StructField("productId", StringType(), True),
    StructField("ts", StringType(), True)  # will cast to timestamp below
])

# ---------- Read from Kafka ----------
kafka_bootstrap = "localhost:9092"
topic = "clickstream_topic"

raw_df = (spark.readStream
          .format("kafka")
          .option("kafka.bootstrap.servers", kafka_bootstrap)
          .option("subscribe", topic)
          .option("startingOffsets", "latest")   # or "earliest" for replay
          .load()
         )

# raw_df schema: key, value, topic, partition, offset, timestamp, timestampType
# Convert value (binary) to string and parse JSON
json_df = raw_df.selectExpr("CAST(value AS STRING) as json_str")

parsed = json_df.select(from_json(col("json_str"), schema).alias("data")).select("data.*")

# Convert ts string to timestamp type if needed
from pyspark.sql.functions import to_timestamp
parsed = parsed.withColumn("event_ts", to_timestamp(col("ts")))

# ---------- Simple streaming aggregation: count actions in sliding windows ----------
agg = (parsed
       .withWatermark("event_ts", "2 minutes")   # handle late events
       .groupBy(window(col("event_ts"), "1 minute", "30 seconds"), col("action"))
       .count()
      )

# ---------- Write aggregated output to console (for demo) ----------
console_query = (agg.writeStream
                 .outputMode("update")   # update mode for windowed aggregations
                 .format("console")
                 .option("truncate", "false")
                 .option("numRows", 50)
                 .start()
                )

# ---------- Also write raw parsed events to Parquet files (append) ----------
parquet_query = (parsed.writeStream
                 .outputMode("append")
                 .format("parquet")
                 .option("path", "output/raw_clickstream/")   # data sink
                 .option("checkpointLocation", "checkpoints/raw_clickstream_cp")
                 .trigger(processingTime="30 seconds")
                 .start()
                )

# Wait for termination
console_query.awaitTermination()
parquet_query.awaitTermination()
