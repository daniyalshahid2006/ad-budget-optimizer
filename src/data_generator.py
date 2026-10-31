
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from config import RAW_DATA_DIR, DATASET_SIZES, RANDOM_SEED
from platform_profiles import PLATFORM_PROFILES


def generate_dataset(total_rows, chunk_size=100_000):
    rng = np.random.default_rng(RANDOM_SEED)

    output_file = RAW_DATA_DIR / f"marketing_data_{total_rows}.csv"
    platforms = list(PLATFORM_PROFILES.keys())

    first_chunk = True
    generated = 0

    while generated < total_rows:
        rows = min(chunk_size, total_rows - generated)

        platform = rng.choice(
            platforms,
            size=rows,
            p=[0.25, 0.25, 0.20, 0.15, 0.15]
        )

        impressions = rng.integers(500, 50_001, size=rows)

        ctr = np.array([
            PLATFORM_PROFILES[p]["avg_ctr"] for p in platform
        ]) * rng.uniform(0.7, 1.3, size=rows)

        clicks = rng.binomial(impressions, np.clip(ctr, 0, 1))

        conversion_rate = np.array([
            PLATFORM_PROFILES[p]["avg_conversion_rate"]
            for p in platform
        ]) * rng.uniform(0.7, 1.3, size=rows)

        conversions = rng.binomial(
            clicks,
            np.clip(conversion_rate, 0, 1)
        )

        cpm = np.array([
            PLATFORM_PROFILES[p]["avg_cpm"] for p in platform
        ])

        spend = (
            impressions / 1000
            * cpm
            * rng.uniform(0.8, 1.2, size=rows)
        )

        revenue = conversions * rng.uniform(20, 150, size=rows)

        dates = (
            pd.Timestamp("2025-01-01")
            + pd.to_timedelta(
                rng.integers(0, 365, size=rows),
                unit="D"
            )
        )

        df = pd.DataFrame({
            "date": dates,
            "campaign_id": rng.integers(1001, 1101, size=rows),
            "platform": platform,
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
            "spend": np.round(spend, 2),
            "revenue": np.round(revenue, 2),
            "age": rng.integers(18, 66, size=rows),
            "gender": rng.choice(["Male", "Female"], size=rows),
            "city": rng.choice(
                ["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Faisalabad", "Multan"],
                size=rows,
            ),
            "device": rng.choice(
                ["Mobile", "Desktop", "Tablet"],
                size=rows,
                p=[0.65, 0.28, 0.07],
            ),
        })

        df.to_csv(
            output_file,
            mode="w" if first_chunk else "a",
            header=first_chunk,
            index=False
        )

        first_chunk = False
        generated += rows

        print(f"Generated {generated:,} / {total_rows:,} rows")

    print(f"\nDataset saved: {output_file}")
    print(f"Total rows: {generated:,}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate synthetic advertising data"
    )

    parser.add_argument(
        "--rows",
        type=int,
        choices=DATASET_SIZES,
        default=1_000
    )

    args = parser.parse_args()
    generate_dataset(args.rows)

