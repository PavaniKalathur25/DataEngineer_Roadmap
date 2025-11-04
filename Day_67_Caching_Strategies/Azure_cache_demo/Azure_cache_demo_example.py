import redis

# Replace with your Azure Cache for Redis connection details
AZURE_REDIS_HOST = "your-redis-name.redis.cache.windows.net"
AZURE_REDIS_PORT = 6380
AZURE_REDIS_PASSWORD = "your-access-key"

# SSL is required for Azure Redis
cache = redis.StrictRedis(
    host=AZURE_REDIS_HOST,
    port=AZURE_REDIS_PORT,
    password=AZURE_REDIS_PASSWORD,
    ssl=True
)

# Example: storing pipeline metadata
cache.set("pipeline_status", "running")
print("✅ Set pipeline_status in Azure Cache")

status = cache.get("pipeline_status")
print(f"Fetched from Azure Cache → {status.decode('utf-8')}")
