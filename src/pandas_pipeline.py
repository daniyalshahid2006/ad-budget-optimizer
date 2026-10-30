
import time
import pandas as pd

from config import RAW_DATA_DIR, PROCESSED_DATA_DIR
from metrics import calculate_metrics


def run_pandas_pipeline(dataset_size=1000):
    input_file = RAW_DATA_DIR / f"marketing_data_{dataset_size}.csv"
    output_file = PROCESSED_DATA_DIR / f"pandas_results_{dataset_size}.csv"

    start_time = time.perf_counter()

    print(f"Loading dataset: {dataset_size:,} rows")

    df = pd.read_csv(input_file)

    # Calculate performance metrics by platform
    results = []

    for platform, group in df.groupby("platform"):
        metrics = calculate_metrics(group)
        metrics["platform"] = platform
        results.append(metrics)

    result_df = pd.DataFrame(results)

    result_df.to_csv(output_file, index=False)

    execution_time = time.perf_counter() - start_time

    print("\nPANDAS PIPELINE SUCCESSFUL")
    print("=" * 40)
    print(result_df.to_string(index=False))
    print(f"\nExecution time: {execution_time:.4f} seconds")
    print(f"Output saved: {output_file}")

    return execution_time


if __name__ == "__main__":
    run_pandas_pipeline(1000)
