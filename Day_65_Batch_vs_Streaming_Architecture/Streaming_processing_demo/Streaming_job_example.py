"""
Simulated Streaming Job
Reading data in real-time from Kafka-like stream
"""

import time
import random

def generate_stream_data():
    return {"user_id": random.randint(1, 100), "event": random.choice(["click", "view", "purchase"])}

def process_stream():
    print("⚡ Starting Streaming Job...")
    for _ in range(5):
        event = generate_stream_data()
        print(f"📥 New Event: {event}")
        print("✅ Processed in real-time\n")
        time.sleep(1)  # Simulate live data arrival

if __name__ == "__main__":
    process_stream()
