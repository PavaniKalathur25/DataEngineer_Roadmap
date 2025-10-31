# Day 59 — Streaming Mini Project: Kafka → Spark Structured Streaming → Parquet

## Overview
This mini project demonstrates a complete real-time pipeline:
- Python producer sends JSON events to a Kafka topic
- Apache Kafka runs locally (Docker Compose)
- PySpark Structured Streaming reads from Kafka, performs simple ETL (parse JSON, aggregate), writes outputs to Parquet and console
- Checkpointing and parallelism tuning included for production-like behaviour

## Files
- `docker-compose.yml`: Starts Zookeeper + Kafka
- `create_topic.sh`: Helper script to create Kafka topic
- `config/spark_config.json`: Suggested Spark configs for parallelism
- `data/sample_clickstream.json`: Small offline sample used for testing
- `scripts/producer.py`: Python script to produce JSON events to Kafka
- `scripts/spark_consumer.py`: PySpark Structured Streaming consumer (reads from Kafka, processes, writes)
- `scripts/write_to_parquet.py`: Optional script showing Delta/Parquet sink usage
- `checkpoints/`: checkpoint directory used by Spark (created at runtime)

## Prereqs (local)
- Docker & Docker Compose installed
- Java (for Kafka client tools used inside container if needed)
- Python 3.8+ (for producer)
- PySpark (or Spark distribution) for running the streaming consumer
  - When running with `spark-submit`, include Kafka connector packages:
    `--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1` (**match your Spark version**)

## Quick start (local)
1. Start Kafka:
   ```bash
   docker compose up -d

2. Create topic:

chmod +x create_topic.sh
./create_topic.sh clickstream_topic

3. Start the Python producer (in a new terminal):

python3 scripts/producer.py

4. Start the Spark streaming consumer (new terminal). If you have spark-submit:

spark-submit \
  --master local[4] \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1 \
  scripts/spark_consumer.py

5. Stop everything when done:

docker compose down
