# Day 53 – Kafka + Spark ETL on Streaming Data

## 🔹 What is it?
Kafka + Spark ETL is a real-time data pipeline setup where Kafka acts as the source for streaming events and Spark Structured Streaming performs ETL (Extract-Transform-Load) on the data in motion.

---

## 🔹 Where It’s Used
- E-commerce order streaming and live sales analytics  
- IoT data collection and sensor monitoring  
- Fraud detection in financial transactions  
- Log and event pipeline monitoring  
- Streaming ETL to Data Lakes (Azure Data Lake, S3, Delta Lake)

---

## 🔹 Why Used
| Benefit | Description |
|----------|--------------|
| ⚡ Real-time ETL | Process data as soon as it arrives |
| 💾 Reliable & durable | Kafka stores data safely on disk |
| 🧱 Unified framework | Spark handles both batch and stream |
| 🔁 Scalable | Can handle millions of records per minute |
| 📊 Actionable insights | Enable live dashboards and alerts |

---

## 🔹 Core Concepts & Keywords
| Keyword | Meaning |
|----------|----------|
| **ETL** | Extract, Transform, Load data continuously |
| **Kafka Topic** | Channel for streaming events |
| **readStream / writeStream** | Spark methods to read and write live data |
| **Schema** | Structure of incoming data |
| **Checkpoint** | Recovery point for stream state |
| **Sink** | Destination (Data Lake, DB, console) |
| **Micro-batch** | Small time-based batch inside a stream |

---

## 🔹 Simplified Summary
Kafka acts as a real-time messenger.  
Spark Structured Streaming reads data from Kafka, cleans and aggregates it, then writes the results to a storage system or dashboard continuously.  
Together, they form a **real-time ETL pipeline** for live analytics.

---

## 🧰 Code
See `kafka_spark_etl.py` for an example Kafka → Spark → Data Lake pipeline.
