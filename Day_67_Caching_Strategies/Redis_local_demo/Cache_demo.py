---

### 🧩 **redis_local_demo/cache_demo.py**
```python
import redis
from simulate_pipeline import get_product_details

# Connect to local Redis
cache = redis.Redis(host='localhost', port=6379, db=0)

def get_cached_product(product_id):
    # Try to get from cache
    cached_data = cache.get(product_id)
    if cached_data:
        print("✅ Cache Hit")
        return cached_data.decode('utf-8')

    print("❌ Cache Miss - Fetching from pipeline...")
    product_data = get_product_details(product_id)
    cache.setex(product_id, 60, product_data)  # TTL = 60 sec
    return product_data

if __name__ == "__main__":
    print(get_cached_product("P1001"))
    print(get_cached_product("P1001"))  # 2nd time → Cache hit
