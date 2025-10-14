# Day 52 - Spark Structured Streaming: ReadStream Example
# Before running, start a socket server using:
#   nc -lk 9999
# Then type text messages to simulate streaming input.

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReadStreamExample").getOrCreate()

# 1️⃣ Read real-time data from socket
lines = (
    spark.readStream
    .format("socket")
    .option("host", "localhost")
    .option("port", 9999)
    .load()
)

# 2️⃣ Transform data (split words)
words = lines.selectExpr("explode(split(value, ' ')) as word")

# 3️⃣ Word count aggregation
wordCounts = words.groupBy("word").count()

# 4️⃣ Write live output to console
query = (
    wordCounts.writeStream
    .outputMode("complete")
    .format("console")
    .option("truncate", "false")
    .start()
)

query.awaitTermination()
