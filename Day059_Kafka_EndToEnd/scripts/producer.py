#!/usr/bin/env python3
# scripts/producer.py
import json
import time
import random
from datetime import datetime, timezone
from kafka import KafkaProducer

BROKER = "localhost:9092"
TOPIC = "clickstream_topic"

producer = KafkaProducer(
    bootstrap_servers=[BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    acks=1
)

event_types = ["click", "view", "add_to_cart", "purchase"]
pages = ["/home", "/product", "/search", "/checkout"]
product_ids = ["p1","p2","p3","p4", None]

def gen_event():
    return {
        "userId": f"u{random.randint(1,10)}",
        "page": random.choice(pages),
        "action": random.choice(event_types),
        "productId": random.choice(product_ids),
        "ts": datetime.now(timezone.utc).isoformat()
    }

print("Producer started. Sending events to", BROKER, "->", TOPIC)
try:
    while True:
        ev = gen_event()
        producer.send(TOPIC, ev)
        print("Sent:", ev)
        time.sleep(1)  # adjust frequency for testing
except KeyboardInterrupt:
    print("Stopping producer...")
finally:
    producer.flush()
    producer.close()
