from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

def run_eventhub_stream():
    spark = SparkSession.builder.appName("AzureEventHubIntegration").getOrCreate()

    event_hub_connection_string = "Endpoint=sb://<YourNamespace>.servicebus.windows.net/;SharedAccessKeyName=<KeyName>;SharedAccessKey=<Key>;EntityPath=<EventHubName>"

    ehConf = {'eventhubs.connectionString': event_hub_connection_string}

    # Read from Event Hub
    eventhub_df = spark.readStream.format("eventhubs").options(**ehConf).load()

    schema = StructType([
        StructField("deviceId", StringType()),
        StructField("temperature", StringType()),
        StructField("timestamp", TimestampType())
    ])

    parsed_df = eventhub_df.select(from_json(col("body").cast("string"), schema).alias("data")).select("data.*")

    # Output
    query = parsed_df.writeStream.outputMode("append").format("console").start()
    query.awaitTermination()

if __name__ == "__main__":
    run_eventhub_stream()
