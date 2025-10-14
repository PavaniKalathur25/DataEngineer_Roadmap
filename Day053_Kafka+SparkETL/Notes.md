# Day 53 – Kafka + Spark ETL Quick Notes

## 🔸 Pipeline Flow
Kafka (Producer) → Kafka Topic → Spark Structured Streaming → Transform → Sink (Console, File, DB)

## 🔸 Typical Use Case
E-commerce order streaming:
- Producer sends new orders to Kafka  
- Spark reads them in real time  
- Aggregates sales by region and writes to dashboard  

## 🔸 Common Transformations
- Filtering irrelevant records  
- Parsing JSON/CSV data  
- Aggregating with groupBy()  
- Joining with reference data  
- Window functions for time-based aggregations  

## 🔸 Example Sinks
- Console (for testing)  
- Azure Data Lake / S3  
- Delta tables for real-time analytics  
- Databases (PostgreSQL, Snowflake)  

## 🔸 Keywords to Remember
Kafka | Spark Structured Streaming | ETL | Schema | Checkpoint | Sink | Source | Micro-batch | Fault Tolerance | Real-time Pipeline

💡 Tip: Add `.trigger(processingTime='1 minute')` to control micro-batch intervals.
