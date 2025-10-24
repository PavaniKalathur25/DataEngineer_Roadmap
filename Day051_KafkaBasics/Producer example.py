# Day 51 - Kafka Producer Example
# Before running, make sure Kafka is running on localhost:9092
# Install library: pip install kafka-python

from kafka import KafkaProducer

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send sample messages
for i in range(5):
    message = f"New order #{i+1}".encode('utf-8')
    producer.send('orders', message)
    print(f"✅ Sent: {message}")

# Ensure all messages are sent
producer.flush()
print("🎯 All messages sent successfully!")
