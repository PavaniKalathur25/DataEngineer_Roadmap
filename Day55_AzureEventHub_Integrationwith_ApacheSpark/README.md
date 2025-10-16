# ☁️ Day 55 - Azure Event Hub Integration with Apache Spark

## 🧠 What is Azure Event Hub?

**Azure Event Hub** is a fully managed, real-time **data ingestion service** on Microsoft Azure that can process **millions of events per second**.  
It acts as a **message streaming platform**, similar to Kafka, where Spark can **read and process events** in real time.

---

## ⚙️ Where It's Used
- **IoT Telemetry Streaming** (smart sensors, industrial devices)
- **E-commerce event tracking** (clickstream, order updates)
- **Financial transactions** (real-time fraud detection)
- **Log/Telemetry ingestion** (application and infrastructure monitoring)
- **Data pipelines** (Event Hub → Spark → Data Lake)

---

## 💡 Why Used
- To **connect streaming event sources** directly to Spark for analysis or transformation.
- For **real-time analytics** instead of waiting for batch jobs.
- To **decouple data producers** and **consumers** efficiently.
- Event Hub provides **scalability**, **fault tolerance**, and **replay support**.

---

## 🧩 Architecture Overview
