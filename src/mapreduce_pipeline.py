
import csv
import time
from collections import defaultdict

from config import RAW_DATA_DIR, PROCESSED_DATA_DIR


def mapper(row):
    """Convert each advertising record into a platform-keyed record."""
    platform = row["platform"]

    values = {
        "impressions": int(row["impressions"]),
        "clicks": int(row["clicks"]),
        "conversions": int(row["conversions"]),
        "spend": float(row["spend"]),
        "revenue": float(row["revenue"]),
    }

    return platform, values


def reducer(mapped_records):
    """Combine records and calculate platform metrics."""
    totals = defaultdict(
        lambda: {
            "impressions": 0,
            "clicks": 0,
            "conversions": 0,
            "spend": 0.0,
            "revenue": 0.0,
        }
    )

    for platform, values in mapped_records:
        for key, value in values.items():
            totals[platform][key] += value

    results = []

    for platform, data in totals.items():
        impressions = data["impressions"]
        clicks = data["clicks"]
        conversions = data["conversions"]
        spend = data["spend"]
        revenue = data["revenue"]

        results.append({
            "platform": platform,
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
            "spend": round(spend, 2),
            "revenue": round(revenue, 2),
            "CTR (%)": round(clicks / impressions * 100, 2)
                if impressions else 0,
            "CPC": round(spend / clicks, 2) if clicks else 0,
            "CPM": round(spend / impressions * 1000, 2)
                if impressions else 0,
            "Conversion Rate (%)": round(conversions / clicks * 100, 2)
                if clicks else 0,
            "ROAS": round(revenue / spend, 2) if spend else 0,
        })

    return results


def run_mapreduce_pipeline(dataset_size=1000):
    input_file = RAW_DATA_DIR / f"marketing_data_{dataset_size}.csv"
    output_file = PROCESSED_DATA_DIR / f"mapreduce_results_{dataset_size}.csv"

    start_time = time.perf_counter()

    print(f"Loading dataset: {dataset_size:,} rows")

    mapped_records = []

    with open(input_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            mapped_records.append(mapper(row))

    results = reducer(mapped_records)

    fieldnames = list(results[0].keys())

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    execution_time = time.perf_counter() - start_time

    print("\nMAPREDUCE PIPELINE SUCCESSFUL")
    print("=" * 40)

    for result in results:
        print(result)

    print(f"\nExecution time: {execution_time:.4f} seconds")
    print(f"Output saved: {output_file}")

    return execution_time


if __name__ == "__main__":
    run_mapreduce_pipeline(1000)
