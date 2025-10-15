---

### 📓 **notebooks/Day54_Watermarking_LateDataHandling.ipynb**

```python
# Day 54 - Watermarking & Late Data Handling
# Spark Structured Streaming Example

from pyspark.sql import SparkSession
from pyspark.sql.functions import window, col, from_json
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType

# 1️⃣ Create Spark Session
spark = SparkSession.builder.appName("WatermarkExample").getOrCreate()

# 2️⃣ Define schema for sensor data
schema = StructType([
    StructField("sensor_id", IntegerType()),
    StructField("temperature", IntegerType()),
    StructField("timestamp", TimestampType())
])

# 3️⃣ Read JSON stream (simulate or replace with Kafka)
sensor_df = spark.readStream \
    .schema(schema) \
    .json("data/sample_sensor_data.json")

# 4️⃣ Apply watermark and window aggregation
watermarked_df = sensor_df \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(window(col("timestamp"), "5 minutes")) \
    .avg("temperature")

# 5️⃣ Write to console (or sink)
query = watermarked_df.writeStream \
    .outputMode("update") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()
