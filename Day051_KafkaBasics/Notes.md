# Day 51 – Kafka Basics: Quick Notes

## Core Concepts
- Kafka = distributed, fault-tolerant, real-time event streaming platform.
- Producers push data → Topics → Consumers pull data.
- Works best in scalable, decoupled systems.

## Common Interview Keywords
Topic | Partition | Broker | Offset | Consumer Group | Replication | Fault Tolerance | Event Stream

## Commands (CLI)
```bash
# Start Zookeeper (older versions)
zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka Broker
kafka-server-start.sh config/server.properties

# Create a topic
kafka-topics.sh --create --topic orders --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# List topics
kafka-topics.sh --list --bootstrap-server localhost:9092
