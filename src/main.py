
from config import DATASET_SIZES
from benchmark import ensure_datasets
from pandas_pipeline import run_pandas_pipeline
from mapreduce_pipeline import run_mapreduce_pipeline
from spark_pipeline import run_spark_pipeline
from recommendation import generate_recommendations


def main():
    print("\n" + "=" * 60)
    print("AD BUDGET OPTIMIZER")
    print("=" * 60)

    # Generate datasets only when missing
    ensure_datasets()

    # Run all three processing approaches
    pipelines = {
        "Pandas": run_pandas_pipeline,
        "MapReduce": run_mapreduce_pipeline,
        "Spark": run_spark_pipeline,
    }

    for size in DATASET_SIZES:
        print(f"\nPROCESSING DATASET: {size:,} ROWS")

        for name, pipeline in pipelines.items():
            print(f"\nRunning {name}...")
            pipeline(size)

    # Generate platform recommendations
    generate_recommendations()

    print("\nPROJECT EXECUTION COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
