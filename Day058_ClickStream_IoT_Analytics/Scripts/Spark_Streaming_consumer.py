from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col

spark = SparkSession.builder \
    .appName("Clickstream_IoT_Streaming") \
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

agg_df = parsed_df.groupBy("eventType").avg("value")

query = agg_df.writeStream \
    .format("console") \
    .outputMode("complete") \
    .trigger(processingTime="10 seconds") \
    .start()

query.awaitTermination()
