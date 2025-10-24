import requests
import json
import random
import time

# 🔗 Power BI Streaming Dataset API URL (replace with your own)
url = "https://api.powerbi.com/beta/<your_workspace_id>/datasets/<dataset_id>/rows?key=<api_key>"

while True:
    # Simulating random sales data
    data = [{
        "region": random.choice(["North", "South", "East", "West"]),
        "sales": random.randint(500, 1500),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }]
    
    # Sending to Power BI REST API
    requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    print("✅ Data sent:", data)
    
    time.sleep(5)  # every 5 seconds
