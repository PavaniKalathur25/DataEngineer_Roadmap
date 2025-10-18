# Day 57 – Streaming Optimization: Parallelism & Checkpointing

This module focuses on optimizing **Spark Structured Streaming** jobs using
**parallelism** and **checkpointing**.

### 🔍 Topics Covered
- What is Parallelism
- Why Parallelism is important in streaming
- How Checkpointing ensures fault tolerance
- How to tune streaming queries for performance

---

## ⚙️ Setup Instructions
1. Configure SparkSession with optimal shuffle partitions.
2. Enable checkpointing for streaming queries.
3. Run the scripts to observe improved processing speed and recovery.

---

## 📂 Files
- `scripts/parallelism_tuning.py` → Demonstrates Spark parallelism configs.
- `scripts/checkpointing_example.py` → Demonstrates checkpointed streaming.
- `spark_parallelism_checkpointing.ipynb` → Notebook for testing end-to-end.

---

## 🧠 Keywords
`parallelism`, `checkpointing`, `fault-tolerance`, `shufflePartitions`, `streaming optimization`, `structured streaming`, `throughput`, `micro-batch interval`
