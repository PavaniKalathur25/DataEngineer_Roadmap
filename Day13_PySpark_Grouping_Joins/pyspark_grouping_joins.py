from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# -------------------------
# 1. Start SparkSession
# -------------------------
spark = SparkSession.builder \
    .appName("Day13_PySpark_Grouping_Joins") \
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
# 3. groupBy()
# -------------------------
print("👉 Count employees per department:")
employees.groupBy("department").count().show()

# -------------------------
# 4. agg()
# -------------------------
print("👉 Average and Max salary per department:")
employees.groupBy("department").agg(
    F.avg("salary").alias("avg_salary"),
    F.max("salary").alias("max_salary")
).show()

# -------------------------
# 5. count()
# -------------------------
print("👉 Total number of employees:")
print("Count =", employees.count())

# -------------------------
# 6. joins
# -------------------------
print("👉 Inner Join Employees with Departments:")
employees.join(departments, employees["department"] == departments["dept_id"], "inner").show()

print("👉 Left Join:")
employees.join(departments, employees["department"] == departments["dept_id"], "left").show()

print("👉 Full Outer Join:")
employees.join(departments, employees["department"] == departments["dept_id"], "outer").show()

# -------------------------
# 7. Stop Spark
# -------------------------
spark.stop()
print("✅ SparkSession stopped!")
