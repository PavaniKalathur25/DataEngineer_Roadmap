import time
import random
from concurrent.futures import ThreadPoolExecutor

def task(name):
    print(f"Starting task {name}...")
    if random.choice([True, False]):  # 50% chance to fail
        raise Exception(f"Task {name} failed ❌")
    time.sleep(2)
    print(f"Task {name} completed ✅")
    return f"Result of {name}"

def run_with_retry(name, retries=3, delay=2):
    attempt = 1
    while attempt <= retries:
        try:
            return task(name)
        except Exception as e:
            print(f"{e} → Retrying {name} (Attempt {attempt}/{retries})...")
            attempt += 1
            time.sleep(delay)
    print(f"Task {name} failed after {retries} retries ❌")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(run_with_retry, ["Task1", "Task2", "Task3"]))
    print("All tasks attempted.")
