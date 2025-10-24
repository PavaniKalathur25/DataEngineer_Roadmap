# Day 51 - Kafka Consumer Example
# Before running, ensure Kafka topic 'orders' has messages
# Install library: pip install kafka-python

from kafka import KafkaConsumer

# Create a Kafka consumer
consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='order-consumers'
)

print("📥 Listening for messages...")
for message in consumer:
    print(f"🧾 Received: {message.value.decode('utf-8')}")
