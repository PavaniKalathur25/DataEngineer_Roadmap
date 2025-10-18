from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("StreamingParallelismTuning") \
    .getOrCreate()

# Example of tuning parallelism
spark.conf.set("spark.sql.shuffle.partitions", 8)
spark.conf.set("spark.default.parallelism", 8)

print("Parallelism Configurations:")
print("Shuffle Partitions:", spark.conf.get("spark.sql.shuffle.partitions"))
print("Default Parallelism:", spark.conf.get("spark.default.parallelism"))

# Simulate simple transformation with parallel processing
data = spark.read.json("data/sample_stream_data.json")
transformed = data.groupBy("eventType").count()

transformed.show()
