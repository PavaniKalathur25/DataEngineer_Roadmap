import time
import json
import random
from datetime import datetime

users = ["Alice", "Bob", "Charlie", "David"]
actions = ["click", "scroll", "purchase", "logout"]

def generate_event():
    return {
        "user": random.choice(users),
        "action": random.choice(actions),
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    print("Starting event stream simulation...\n")
    while True:
        event = generate_event()
        print(json.dumps(event))
        time.sleep(2)  # simulate real-time events every 2 seconds
