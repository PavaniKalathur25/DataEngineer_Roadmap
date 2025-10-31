#!/usr/bin/env python3
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_timestamp
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder \
    .appName("ClickstreamToParquet") \
    .config("spark.sql.shuffle.partitions", 8) \
    .getOrCreate()

schema = StructType([
    StructField("userId", StringType()),
    StructField("page", StringType()),
    StructField("action", StringType()),
    StructField("productId", StringType()),
    StructField("ts", StringType())
])

df = (spark.readStream.format("kafka")
      .option("kafka.bootstrap.servers", "localhost:9092")
      .option("subscribe", "clickstream_topic")
      .load())

parsed = df.selectExpr("CAST(value AS STRING) as json_str")
parsed = parsed.select(from_json(col("json_str"), schema).alias("data")).select("data.*")
parsed = parsed.withColumn("event_ts", to_timestamp(col("ts")))

query = (parsed.writeStream
         .format("parquet")
         .option("path", "output/clickstream_parquet")
         .option("checkpointLocation", "checkpoints/clickstream_parquet_cp")
         .trigger(processingTime="1 minute")
         .outputMode("append")
         .start())

query.awaitTermination()
