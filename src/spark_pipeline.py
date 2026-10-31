import os
import sys
import time
from pathlib import Path

import pandas as pd
import pyspark

# Explicitly configure Spark's installation directory
os.environ["SPARK_HOME"] = str(
    Path(pyspark.__file__).resolve().parent
)

# Use the Python interpreter from the activated virtual environment
os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    sum as spark_sum,
    round as spark_round,
    when
)

from config import RAW_DATA_DIR, PROCESSED_DATA_DIR

def run_spark_pipeline(dataset_size=1000):
    python_path = os.path.normpath(sys.executable)

    os.environ["PYSPARK_PYTHON"] = python_path
    os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

    input_file = RAW_DATA_DIR / f"marketing_data_{dataset_size}.csv"
    output_file = PROCESSED_DATA_DIR / f"spark_results_{dataset_size}.csv"

    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    start_time = time.perf_counter()

    spark = (
        SparkSession.builder
        .appName("AdBudgetOptimizer")
        .master("local[*]")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    try:
        print(f"Loading dataset: {dataset_size:,} rows")

        df = spark.read.csv(
            str(input_file),
            header=True,
            inferSchema=True
        )

        results = (
            df.groupBy("platform")
            .agg(
                spark_sum("impressions").alias("impressions"),
                spark_sum("clicks").alias("clicks"),
                spark_sum("conversions").alias("conversions"),
                spark_round(spark_sum("spend"), 2).alias("spend"),
                spark_round(spark_sum("revenue"), 2).alias("revenue")
            )
            .withColumn(
                "CTR (%)",
                spark_round(
                    when(
                        col("impressions") > 0,
                        col("clicks") / col("impressions") * 100
                    ).otherwise(0),
                    2
                )
            )
            .withColumn(
                "CPC",
                spark_round(
                    when(
                        col("clicks") > 0,
                        col("spend") / col("clicks")
                    ).otherwise(0),
                    2
                )
            )
            .withColumn("CPA", spark_round(when(col("conversions") > 0, col("spend") / col("conversions")).otherwise(0), 2)).withColumn("CPM",
                spark_round(
                    when(
                        col("impressions") > 0,
                        col("spend") / col("impressions") * 1000
                    ).otherwise(0),
                    2
                )
            )
            .withColumn(
                "Conversion Rate (%)",
                spark_round(
                    when(
                        col("clicks") > 0,
                        col("conversions") / col("clicks") * 100
                    ).otherwise(0),
                    2
                )
            )
            .withColumn(
                "ROAS",
                spark_round(
                    when(
                        col("spend") > 0,
                        col("revenue") / col("spend")
                    ).otherwise(0),
                    2
                )
            )
            .orderBy("platform")
        )

        rows = results.collect()

        print("\nSPARK PIPELINE SUCCESSFUL")
        print("=" * 40)

        for row in rows:
            print(row.asDict())

        results_df = pd.DataFrame(
            [row.asDict() for row in rows]
        )

        results_df.to_csv(output_file, index=False)

        print(f"Output saved: {output_file}")

    finally:
        spark.stop()

    execution_time = time.perf_counter() - start_time

    print(f"\nExecution time: {execution_time:.4f} seconds")

    return execution_time


if __name__ == "__main__":
    run_spark_pipeline(1000)

