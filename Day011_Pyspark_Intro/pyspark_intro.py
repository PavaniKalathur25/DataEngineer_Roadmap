from pyspark.sql import SparkSession

# -------------------------
# 1. Start SparkSession
# -------------------------
spark = SparkSession.builder     .appName(Day11_PySpark_Intro)     .getOrCreate()

print(✅ SparkSession created!)

# -------------------------
# 2. RDD Example
# -------------------------
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
print(RDD Collect:, rdd.collect())

# -------------------------
# 3. DataFrame Example
# -------------------------
df = spark.createDataFrame(
    [(1, Alice, 50000), (2, Bob, 70000), (3, Charlie, 40000)],
    [id, name, salary]
)
df.show()

# Simple query
df.filter(df[salary] > 50000).show()

# -------------------------
# 4. Reading Data
# -------------------------

# CSV
df_csv = spark.read.option(header, true).csv(data/employees.csv)
print(CSV Data:)
df_csv.show()

# Parquet
df_parquet = spark.read.parquet(data/employees.parquet)
print(Parquet Data:)
df_parquet.show()

# JSON
df_json = spark.read.json(data/employees.json)
print(JSON Data:)
df_json.show()

# -------------------------
# 5. Stop Session
# -------------------------
spark.stop()

