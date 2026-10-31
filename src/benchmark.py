
import time
import pandas as pd

from config import (
    RAW_DATA_DIR,
    BENCHMARK_DIR,
    DATASET_SIZES,
    BENCHMARK_RUNS,
)

from data_generator import generate_dataset
from pandas_pipeline import run_pandas_pipeline
from mapreduce_pipeline import run_mapreduce_pipeline
from spark_pipeline import run_spark_pipeline


def ensure_datasets():
    """Generate missing datasets automatically."""

    for size in DATASET_SIZES:
        dataset = RAW_DATA_DIR / f"marketing_data_{size}.csv"

        if not dataset.exists():
            print(f"\nGenerating missing dataset: {size:,} rows")
            generate_dataset(size)
        else:
            print(f"Dataset available: {size:,} rows")


def run_benchmark():

    ensure_datasets()

    results = []

    pipelines = {
        "Pandas": run_pandas_pipeline,
        "MapReduce": run_mapreduce_pipeline,
        "Spark": run_spark_pipeline,
    }

    for size in DATASET_SIZES:

        print("\n" + "=" * 60)
        print(f"BENCHMARKING DATASET: {size:,} ROWS")
        print("=" * 60)

        for pipeline_name, pipeline_function in pipelines.items():

            execution_times = []

            for run in range(1, BENCHMARK_RUNS + 1):

                print(
                    f"\n{pipeline_name} | "
                    f"Run {run}/{BENCHMARK_RUNS}"
                )

                elapsed = pipeline_function(size)
                execution_times.append(elapsed)

                print(f"Completed in {elapsed:.4f} seconds")

            results.append({
                "dataset_size": size,
                "pipeline": pipeline_name,
                "run_1_seconds": round(execution_times[0], 4),
                "run_2_seconds": round(execution_times[1], 4),
                "run_3_seconds": round(execution_times[2], 4),
                "average_time_seconds": round(
                    sum(execution_times) / len(execution_times), 4
                ),
                "minimum_time_seconds": round(min(execution_times), 4),
                "maximum_time_seconds": round(max(execution_times), 4),
                "runs": len(execution_times),
            })

    results_df = pd.DataFrame(results)

    output_file = BENCHMARK_DIR / "benchmark_results.csv"
    results_df.to_csv(output_file, index=False)

    print("\n" + "=" * 60)
    print("BENCHMARKING COMPLETED")
    print("=" * 60)

    print(results_df.to_string(index=False))
    print(f"\nResults saved: {output_file}")


if __name__ == "__main__":
    run_benchmark()
