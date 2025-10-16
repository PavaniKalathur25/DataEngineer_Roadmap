---

## 💻 PySpark Example — Read Stream from Azure Event Hub

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

# Step 1: Create Spark Session
spark = SparkSession.builder.appName("EventHubIntegration").getOrCreate()

# Step 2: Define Event Hub connection string
event_hub_connection_string = "Endpoint=sb://<YourNamespace>.servicebus.windows.net/;SharedAccessKeyName=<KeyName>;SharedAccessKey=<Key>;EntityPath=<EventHubName>"

# Step 3: Configure Event Hub
ehConf = {
  'eventhubs.connectionString': event_hub_connection_string
}

# Step 4: Read stream from Event Hub
eventhub_df = spark.readStream.format("eventhubs").options(**ehConf).load()

# Step 5: Define schema
schema = StructType([
    StructField("deviceId", StringType()),
    StructField("temperature", StringType()),
    StructField("timestamp", TimestampType())
])

# Step 6: Parse JSON body
parsed_df = eventhub_df.select(from_json(col("body").cast("string"), schema).alias("data")).select("data.*")

# Step 7: Write stream to console (can be Data Lake, SQL, etc.)
query = parsed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
