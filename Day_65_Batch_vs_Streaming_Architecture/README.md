# 🧩 Day 65 – Batch vs Streaming Architecture (Lambda & Kappa Architecture)

## 📘 Overview
Data can be processed in two major ways:  
**Batch** (in large chunks) or **Streaming** (in real-time).  
Lambda and Kappa are the two main architectures that define how these systems coexist or simplify processing.

---

### 🔹 Batch Processing
Processes data in **fixed intervals** — daily, hourly, etc.  
✅ Best for historical trends, reports, and analytics.  
🧰 Tools: Azure Data Factory, Spark, SQL, Databricks, Airflow.

---

### 🔹 Streaming Processing
Continuously processes **real-time data** as it arrives.  
✅ Best for fraud detection, IoT, monitoring, and real-time dashboards.  
🧰 Tools: Kafka, Spark Streaming, Azure Event Hubs, Flink.

---

### 🔹 Lambda Architecture
Combination of **Batch + Streaming** layers:  
- **Batch Layer:** Stores and recomputes master data periodically.  
- **Speed Layer:** Handles recent, real-time data.  
- **Serving Layer:** Merges both to provide accurate + fresh data.

🧠 Example:  
E-commerce system that updates sales dashboards instantly (stream)  
and recalculates totals overnight (batch).

---

### 🔹 Kappa Architecture
Simplified version of Lambda —  
only **Streaming Layer** is used (no separate batch layer).  
All data (historical + real-time) is treated as a stream.

🧠 Example:  
IoT sensor platform where all data arrives in Kafka and processed continuously.

---

### ⚙️ Why Important
- **Batch:** Accuracy  
- **Streaming:** Freshness  
- **Lambda:** Both combined  
- **Kappa:** Simplicity and consistency

---

### 🧠 Keywords
Batch Processing • Streaming • Latency • Throughput • ETL • Event Stream •  
Stateful Processing • Lambda • Kappa • Data Lake • Idempotent
