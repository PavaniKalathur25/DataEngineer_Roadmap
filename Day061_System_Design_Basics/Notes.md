# 🧠 Day 61: System Design Basics — Scalability, Latency, and Throughput

## What is System Design?
System Design is about planning **how system components work together efficiently** — databases, APIs, pipelines, caches, and storage.  
It ensures a system is **reliable, scalable, and high-performing** when data and users grow.

---

## ⚙️ Scalability
**Definition:** Ability of a system to handle **increased load (data, users, or requests)** without breaking.

**Where it’s used:**
- Expanding Kafka topics for higher message volume  
- Scaling Databricks clusters  
- Sharding databases for user data  

**Why used:** To grow smoothly as business or traffic increases.  

**Coding:** Usually configuration-level, but you design code (partitioning, parallelism) to support scaling.  

### 🔑 Keywords
| Keyword | One-line Meaning |
|----------|------------------|
| **Horizontal Scaling** | Add more machines to share the load. |
| **Vertical Scaling** | Upgrade one machine’s CPU/RAM. |
| **Load Balancer** | Distributes traffic evenly across servers. |
| **Partitioning** | Divide data into smaller chunks for parallel work. |
| **Replication** | Keep multiple data copies for reliability. |
| **Elasticity** | Auto-scale up or down based on usage. |

---

## ⚡ Latency
**Definition:** The time delay between sending a request and receiving a response — “how fast it reacts.”

**Where it’s used:**
- Streaming pipelines  
- Database query response  
- Real-time dashboards  

**Why used:** Ensures **real-time responsiveness** for users or analytics.  

**Coding:** Optimize using caching (Redis), async calls, and faster I/O.

### 🔑 Keywords
| Keyword | One-line Meaning |
|----------|------------------|
| **Response Time** | Time from request to response. |
| **Network Delay** | Time data travels over the network. |
| **Caching** | Store data temporarily for faster reuse. |
| **Asynchronous** | Run tasks without waiting. |
| **Real-Time** | Process data instantly. |
| **Low-Latency** | Millisecond-level fast response. |

---

## 📈 Throughput
**Definition:** Amount of data or work processed per unit time — “how much it handles per second.”

**Where it’s used:**
- Kafka → Messages per second  
- Spark → Rows transformed per minute  
- Databases → Queries per second  

**Why used:** Measures system’s efficiency under load.

**Coding:** Tune parallelism, batch size, and partition count.

### 🔑 Keywords
| Keyword | One-line Meaning |
|----------|------------------|
| **Requests/sec** | Number of API calls handled per second. |
| **Messages/sec** | Kafka messages processed per second. |
| **Batch Size** | Records processed together in one batch. |
| **Parallelism** | Running multiple tasks simultaneously. |
| **Throughput Optimization** | Designing to handle more data faster. |

---

## 💡 Real-world Example
**E-commerce Clickstream Pipeline:**
1. User clicks generate Kafka events.  
2. Spark Streaming processes them in near real-time.  
3. Results stored in Azure Synapse for dashboards.  

| Concept | Example | Goal |
|----------|----------|------|
| Scalability | Add Spark executors or Kafka partitions | Handle more users |
| Latency | Minimize delay to update dashboards | Real-time data |
| Throughput | Increase processed messages/sec | Efficiency |

---

🧠 **Memory Hack**
> **Scalability →** Can it grow?  
> **Latency →** How fast?  
> **Throughput →** How much per second?
