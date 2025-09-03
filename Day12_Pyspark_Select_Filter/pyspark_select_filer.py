from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# -------------------------
# 1. Start SparkSession
# -------------------------
spark = SparkSession.builder \
    .appName("Day12_PySpark_Select_Filter") \
    .getOrCreate()

print("✅ SparkSession started!")

# -------------------------
# 2. Load Sample Data (CSV)
# -------------------------
df = spark.read.option("header", "true").option("inferSchema", "true").csv("data/employees.csv")
print("Input Data:")
df.show()

# -------------------------
# 3. select()
# -------------------------
print("👉 Select only name and salary:")
df.select("name", "salary").show()

# -------------------------
# 4. filter()
# -------------------------
print("👉 Filter employees with salary > 50000:")
df.filter(df["salary"] > 50000).show()

# -------------------------
# 5. withColumn()
# -------------------------
print("👉 Add a new column 'bonus' (10% of salary):")
df_bonus = df.withColumn("bonus", col("salary") * 0.1)
df_bonus.show()

# -------------------------
# 6. drop()
# -------------------------
print("👉 Drop the 'department' column:")
df_dropped = df.drop("department")
df_dropped.show()

# -------------------------
# 7. Stop Spark
# -------------------------
spark.stop()
print("✅ SparkSession stopped!")
