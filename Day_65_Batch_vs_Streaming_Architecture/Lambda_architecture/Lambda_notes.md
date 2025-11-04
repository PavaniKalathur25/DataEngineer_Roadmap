# ⚙️ Lambda Architecture

Lambda = Batch Layer + Speed Layer + Serving Layer

### 1. Batch Layer
- Stores all master data (immutable)
- Periodically recomputes results
- Example: Daily ETL with PySpark + Data Lake

### 2. Speed Layer
- Handles streaming data for real-time updates
- Example: Kafka → Spark Structured Streaming

### 3. Serving Layer
- Combines outputs from batch + stream layers for unified view
- Example: Power BI dashboard combining historical + live data

✅ **Pros:** Accurate, fault-tolerant, scalable  
⚠️ **Cons:** Complex — two separate code paths to maintain
