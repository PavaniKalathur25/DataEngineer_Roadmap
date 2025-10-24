from pyspark.sql import SparkSession

# -------------------------
# 1. Start SparkSession
# -------------------------
spark = SparkSession.builder \
    .appName("Day14_PySpark_Joins") \
    .getOrCreate()

print("✅ SparkSession started!")

# -------------------------
# 2. Load Sample Data
# -------------------------
employees = spark.read.option("header", "true").option("inferSchema", "true").csv("data/employees.csv")
departments = spark.read.option("header", "true").option("inferSchema", "true").csv("data/departments.csv")

print("Employees Data:")
employees.show()

print("Departments Data:")
departments.show()

# -------------------------
# 3. Inner Join
# -------------------------
print("👉 Inner Join (only matching rows):")
inner_df = employees.join(departments, employees["department"] == departments["dept_id"], "inner")
inner_df.show()

# -------------------------
# 4. Outer Join
# -------------------------
print("👉 Outer Join (all rows, unmatched = null):")
outer_df = employees.join(departments, employees["department"] == departments["dept_id"], "outer")
outer_df.show()

# -------------------------
# 5. Cross Join
# -------------------------
print("👉 Cross Join (Cartesian product):")
cross_df = employees.crossJoin(departments)
cross_df.show(10, truncate=False)  # show only 10 rows

# -------------------------
# 6. Stop Spark
# -------------------------
spark.stop()
print("✅ SparkSession stopped!")
