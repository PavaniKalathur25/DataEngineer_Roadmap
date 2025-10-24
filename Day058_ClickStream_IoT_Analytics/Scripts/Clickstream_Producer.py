from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

event_types = ["click", "view", "purchase", "temperature", "humidity"]

print("🚀 Sending Clickstream / IoT events...")

while True:
    event = {
        "deviceId": f"D{random.randint(1,5)}",
        "eventType": random.choice(event_types),
        "value": round(random.uniform(10,100), 2),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    producer.send("clickstream_topic", event)
    print("Sent:", event)
    time.sleep(2)
