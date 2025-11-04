# Simulating Kafka topic replication metadata setup

topic_config = {
    "topic_name": "orders_topic",
    "partitions": 3,
    "replication_factor": 2
}

print(f"Creating topic: {topic_config['topic_name']}")
print(f"Partitions: {topic_config['partitions']}")
print(f"Replication factor: {topic_config['replication_factor']}")

if topic_config["replication_factor"] > 1:
    print("✅ Data durability ensured via replication.")
else:
    print("⚠️ Risk of data loss! Only one replica exists.")
