from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# -------------------------
# 1. Start SparkSession
# -------------------------
spark = SparkSession.builder \
    .appName("Day15_PySpark_WindowFunctions") \
    .getOrCreate()

print("✅ SparkSession started!")

# -------------------------
# 2. Load Sample Data
# -------------------------
employees = spark.read.option("header", "true").option("inferSchema", "true").csv("data/employees.csv")

print("Employees Data:")
employees.show()

# -------------------------
# 3. Define Window Spec
# -------------------------
window_spec = Window.partitionBy("department").orderBy(F.desc("salary"))

# -------------------------
# 4. rank()
# -------------------------
print("👉 Rank employees by salary within department:")
employees.withColumn("rank", F.rank().over(window_spec)).show()

# -------------------------
# 5. row_number()
# -------------------------
print("👉 Assign row_number (for deduplication or strict ordering):")
employees.withColumn("row_number", F.row_number().over(window_spec)).show()

# -------------------------
# 6. Deduplication Example
# -------------------------
print("👉 Keep only top earning employee per department (using row_number):")
deduped = employees.withColumn("row_number", F.row_number().over(window_spec)) \
                   .filter("row_number = 1") \
                   .drop("row_number")
deduped.show()

# -------------------------
# 7. Stop Spark
# -------------------------
spark.stop()
print("✅ SparkSession stopped!")
