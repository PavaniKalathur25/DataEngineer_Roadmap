# Day 51 – Apache Kafka Basics (Producers & Consumers)

## 🔹 What is Kafka?
Apache Kafka is an open-source distributed event streaming platform used for building real-time data pipelines and streaming applications. It enables data to move between systems instantly and reliably.

---

## 🔹 Where It’s Used
- Real-time data pipelines and ETL
- Event-driven microservices
- Monitoring and logging systems
- Real-time analytics dashboards
- IoT or sensor data streaming

**Example:**  
E-commerce system sends order data → Kafka topic → consumer updates billing/inventory in real-time.

---

## 🔹 Why Kafka?
| Benefit | Description |
|----------|--------------|
| ⚡ High Throughput | Handles millions of messages per second |
| 💾 Durable | Messages safely stored on disk |
| 🔁 Scalable | Easily add brokers as load increases |
| 🧱 Decoupled | Producers and consumers are independent |
| ⏱️ Real-time | Data flows continuously between systems |

---

## 🔹 Core Components
| Keyword | Description |
|----------|--------------|
| **Topic** | Channel where messages are published |
| **Producer** | Application that sends data |
| **Consumer** | Application that reads data |
| **Broker** | Kafka server handling topics |
| **Partition** | Topic subdivision for parallelism |
| **Offset** | Message position in a partition |
| **Consumer Group** | Multiple consumers sharing load |

---

## 🧠 Summary
Kafka acts like a **real-time post office**:
- **Producer** → sends messages  
- **Topic** → stores messages  
- **Broker** → manages storage/delivery  
- **Consumer** → receives messages  

---

## 🧰 Coding Examples
See `producer_example.py` and `consumer_example.py` for hands-on Python Kafka usage.
