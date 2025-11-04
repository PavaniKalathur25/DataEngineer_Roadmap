# Day 67 – Caching Strategies (Redis & Azure Cache for Redis)

## 🔹 Topics Covered
- What caching is and why it’s important for Data Engineers
- How Redis and Azure Cache for Redis improve performance
- Sample Python scripts to store and retrieve data

---

## 📘 1. Redis Local Demo
Redis is an in-memory data store used for quick data access.  
Use it to cache lookups, configurations, and processed results in pipelines.

### Run
```bash
cd redis_local_demo
pip install -r requirements.txt
python cache_demo.py
