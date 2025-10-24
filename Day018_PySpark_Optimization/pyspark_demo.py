from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

# -------------------------
# 1. Start SparkSession
# -------------------------
spark = SparkSession.builder \
    .appName("Day18_PySpark_Optimization") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

print("✅ SparkSession started!")

# -------------------------
# 2. Load Data
# -------------------------
transactions = spark.read.option("header", "true").option("inferSchema", "true").csv("data/transactions.csv")
customers = spark.read.option("header", "true").option("inferSchema", "true").csv("data/customers.csv")

print("Transactions Data:")
transactions.show(5)
print("Customers Data:")
customers.show()

# -------------------------
# 3. Catalyst Optimizer Demo
# -------------------------
print("\n👉 Catalyst Optimizer automatically optimizes query plan")
optimized = transactions.filter("amount > 500").select("txn_id", "cust_id", "amount")
optimized.explain(True)  # print logical + physical plan

# -------------------------
# 4. Caching Demo
# -------------------------
print("\n👉 Caching transactions DataFrame for reuse")
transactions.cache()
print("Count with cache:", transactions.count())  # triggers action & cache
print("Reusing cached data...")
print("High-value transactions (> 1000):", transactions.filter("amount > 1000").count())

# -------------------------
# 5. Tungsten Demo
# -------------------------
print("\n👉 Tungsten is automatic (whole-stage codegen, off-heap memory).")
# We can see it in physical plan
optimized.explain(True)

# -------------------------
# 6. Broadcast Join Demo
# -------------------------
print("\n👉 Broadcast Join (small customers table):")
joined = transactions.join(broadcast(customers), "cust_id")
joined.show(5)

# -------------------------
# 7. Stop Spark
# -------------------------
spark.stop()
print("✅ SparkSession stopped!")
