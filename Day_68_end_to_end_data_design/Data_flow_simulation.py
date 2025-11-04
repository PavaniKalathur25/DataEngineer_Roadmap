import time

def ingest():
    print("📥 Ingesting data from API & Kafka...")
    time.sleep(1)
    return {"user": "Pavani", "action": "purchase", "amount": 1200}

def process(data):
    print("⚙️ Processing data (cleaning + transformation)...")
    time.sleep(1)
    data["status"] = "processed"
    data["amount_with_tax"] = round(data["amount"] * 1.18, 2)
    return data

def store(data):
    print("💾 Storing processed data to Azure Data Lake...")
    time.sleep(1)
    data["storage_location"] = "adl://sales-data/2025/"
    return data

def consume(data):
    print("📊 Consuming data via Power BI dashboard...")
    time.sleep(1)
    print(f"✅ Final Data: {data}")

if __name__ == "__main__":
    print("🚀 Starting End-to-End Data Flow Simulation...\n")
    raw = ingest()
    processed = process(raw)
    stored = store(processed)
    consume(stored)
    print("\n🏁 Data Pipeline Completed Successfully!")
