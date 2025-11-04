# ⚡ Kappa Architecture

Kappa simplifies Lambda — no batch layer, only streaming.

### Concept
- Treat all data (past + live) as a continuous stream
- Reprocess old data by replaying events
- Use one codebase for both historical & live data

### Example Flow
Kafka → Spark Streaming → Delta Lake → Power BI

✅ **Pros:** Simpler, no dual maintenance, faster development  
⚠️ **Cons:** Not ideal for extremely large historical reprocessing
