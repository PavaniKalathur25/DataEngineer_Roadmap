"""
Simulated PySpark Batch Job
Processing daily sales data from Data Lake to Warehouse
"""

from datetime import datetime

def run_batch_job():
    print("🧺 Starting Batch Job...")
    print(f"Processing file: sales_{datetime.now().date()}.csv")

    # Simulate transformations
    print("🔄 Aggregating daily totals...")
    print("📦 Writing results to Data Warehouse...")

    print("✅ Batch job completed successfully!")

if __name__ == "__main__":
    run_batch_job()
