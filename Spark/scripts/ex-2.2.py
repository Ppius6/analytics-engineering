from pyspark.sql import SparkSession

schema = """
    id int,
    first string,
    last string,
    url string,
    published string,
    hits int,
    campaigns array <string>
"""

data = [
    [1, "Jules", "Damji", "https://example.com/jules-damji", "2022-01-01", 100, ["twitter", "facebook", "linkedin"]],
    [2, "Jane", "Doe", "https://example.com/jane-doe", "2022-01-02", 200, ["twitter", "facebook", "linkedin"]],
    [3, "Rob", "Smith", "https://example.com/rob-smith", "2022-01-03", 300, ["twitter", "facebook", "linkedin"]],
    [4, "Pieter", "Van de Velde", "https://example.com/pieter-van-de-velde", "2022-01-04", 400, ["twitter", "facebook", "linkedin"]],
    [5, "Pius", "Asamoah", "https://example.com/pius-asamoah", "2022-01-05", 500, ["twitter", "facebook", "linkedin"]],
    [6, "Nana", "Yaa", "https://example.com/nana-yaa", "2022-01-06", 600, ["twitter", "facebook", "linkedin"]],
]

spark = SparkSession.builder.appName("EX-2.2").getOrCreate()

blogs_df = spark.createDataFrame(data, schema=schema)

blogs_df.show()

print(blogs_df.printSchema())