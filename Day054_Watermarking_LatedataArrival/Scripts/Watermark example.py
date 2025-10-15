from pyspark.sql import SparkSession
from pyspark.sql.functions import window, col

def run_watermarking_example():
    spark = SparkSession.builder.appName("WatermarkExample").getOrCreate()

    df = spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "sensor_data") \
        .load()

    parsed_df = df.selectExpr("CAST(value AS STRING)", "timestamp")

    agg_df = parsed_df \
        .withWatermark("timestamp", "10 minutes") \
        .groupBy(window(col("timestamp"), "5 minutes")) \
        .count()

    query = agg_df.writeStream \
        .outputMode("update") \
        .format("console") \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    run_watermarking_example()
