# 🧩 Day 64 – Replication & Fault Tolerance (High Availability, Failover)

## 📘 Overview
Replication and Fault Tolerance ensure systems continue to work even when parts fail.  
They form the backbone of **high availability** and **disaster recovery** in distributed data systems.

### 🔹 Topics Covered
- Replication
- Fault Tolerance
- High Availability
- Failover
- Heartbeat Mechanisms

### 🔸 Real-World Context
- **Kafka:** Topic replication across brokers for message durability  
- **Databases:** Primary–Replica setup in PostgreSQL, MySQL  
- **Azure / AWS:** Auto-failover databases, redundant zones for data lakes  
- **Data Pipelines:** Retry mechanisms and task replication in ADF or Airflow  

---

### ⚙️ Why Important
- Prevents **data loss**
- Maintains **uptime** and **service continuity**
- Ensures **recovery** during hardware or node failure
- Enables **zero downtime deployments**
