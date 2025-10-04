"""
PySpark Example - Reading events from Azure Event Hub in Databricks
"""

event_hub_connection = "<EVENT_HUB_CONNECTION_STRING>"

event_hub_config = {
  'eventhubs.connectionString': sc._jvm.org.apache.spark.eventhubs.EventHubsUtils.encrypt(
    event_hub_connection
  )
}

# Read streaming data from Event Hub
df = spark.readStream.format("eventhubs").options(**event_hub_config).load()

# Convert binary body to string
from pyspark.sql.functions import col
messages = df.select(col("body").cast("string").alias("message"))

# Output stream to console
query = messages.writeStream.outputMode("append").format("console").start()
query.awaitTermination()
