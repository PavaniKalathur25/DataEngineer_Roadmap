from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("CheckpointingExample") \
    .getOrCreate()

# Streaming source (e.g., directory stream)
input_stream = spark.readStream \
    .schema("event STRING, value INT") \
    .json("data/")

# Transformation
aggregated = input_stream.groupBy("event").sum("value")

# Define checkpoint location
checkpoint_dir = "checkpoint/day57_cp"

query = aggregated.writeStream \
    .format("console") \
    .outputMode("complete") \
    .option("checkpointLocation", checkpoint_dir) \
    .trigger(processingTime="10 seconds") \
    .start()

query.awaitTermination()
