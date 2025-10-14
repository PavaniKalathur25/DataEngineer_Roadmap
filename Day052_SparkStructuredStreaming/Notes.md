# Day 52 – Spark Structured Streaming Quick Notes

## 🔸 Key Concepts
- Spark Structured Streaming = real-time version of Spark SQL.
- Works on DataFrames & Datasets.
- Processes continuous data streams with minimal setup.

## 🔸 readStream
Used to continuously read live data from:
- Kafka
- Socket
- Files in a folder (new files trigger updates)

Example:
```python
df = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
