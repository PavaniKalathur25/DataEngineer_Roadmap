# Raw Layer (Bronze)

**What is it?**  
The landing zone of the Data Lake. Stores ingested data as-is (no cleaning, no transformations).

**Where it's actually used?**
- Direct dumps from source systems (databases, APIs, logs, IoT devices).
- Historical storage of raw files for auditing or reprocessing.

**Why used?**
- Keeps a single source of truth for data.
- Useful if you need to reprocess data later.

**Any coding needed?**
Not much; ingestion tools (ADF, Databricks, Kafka) push files here.

**Example Path**
