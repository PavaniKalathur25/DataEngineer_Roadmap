# Day 53 – Kafka + Spark ETL on Streaming Data
# Before running, start Kafka with a topic named 'sales_topic'

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

# 1️⃣ Spark Session
spark = SparkSession.builder.appName("KafkaSparkETL").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# 2️⃣ Read Streaming Data from Kafka
kafka_stream = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "sales_topic")
    .load()
)

# 3️⃣ Define Schema
schema = (
    StructType()
    .add("order_id", StringType())
    .add("product", StringType())
    .add("amount", DoubleType())
    .add("region", StringType())
)

# 4️⃣ Parse JSON Messages
parsed_df = kafka_stream.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# 5️⃣ Transformation – aggregate sales by region
agg_df = parsed_df.groupBy("region").sum("amount").withColumnRenamed("sum(amount)", "total_sales")

# 6️⃣ Write to Console (or replace with file, DB, etc.)
query = (
    agg_df.writeStream
    .outputMode("complete")
    .format("console")
    .option("truncate", "false")
    .option("checkpointLocation", "/tmp/checkpoints/kafka_spark_etl")
    .start()
)

query.awaitTermination()
