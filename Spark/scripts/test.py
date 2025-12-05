from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("TestSparkWSL").master("local[*]").getOrCreate()

print(f"Spark Version: {spark.version}")

data = [("Alice", 34), ("Bob", 45), ("Casty", 30)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

print("\nSample DataFrame: ")
df.show()

print("\nFiltered (Age > 30):")
df.filter(df.Age > 30).show()

spark.stop()
print("\nSpark session closed successfully!")
