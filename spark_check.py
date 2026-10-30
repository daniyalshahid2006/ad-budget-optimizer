
import os
import sys

# Tell Spark which Python executable to use
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("AdBudgetOptimizerTest")
    .master("local[2]")
    .getOrCreate()
)

try:
    data = [
        ("Facebook", 1000),
        ("Instagram", 1500),
        ("Google", 2000),
    ]

    df = spark.createDataFrame(
        data, ["platform", "clicks"]
    )

    df.show()
    print("Spark test successful!")

finally:
    spark.stop()
