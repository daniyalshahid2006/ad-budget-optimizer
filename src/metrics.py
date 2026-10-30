
import pandas as pd
import numpy as np

from config import RAW_DATA_DIR


def calculate_metrics(df):
    impressions = df["impressions"].sum()
    clicks = df["clicks"].sum()
    conversions = df["conversions"].sum()
    spend = df["spend"].sum()
    revenue = df["revenue"].sum()

    return {
        "impressions": impressions,
        "clicks": clicks,
        "conversions": conversions,
        "spend": round(spend, 2),
        "revenue": round(revenue, 2),
        "CTR (%)": round(clicks / impressions * 100, 2)
            if impressions else 0,
        "CPC": round(spend / clicks, 2)
            if clicks else 0,
        "CPM": round(spend / impressions * 1000, 2)
            if impressions else 0,
        "Conversion Rate (%)": round(conversions / clicks * 100, 2)
            if clicks else 0,
        "ROAS": round(revenue / spend, 2)
            if spend else 0,
    }


def main():
    file_path = RAW_DATA_DIR / "marketing_data_1000.csv"

    df = pd.read_csv(file_path)

    print("\nOVERALL MARKETING PERFORMANCE")
    print("=" * 40)

    metrics = calculate_metrics(df)

    for name, value in metrics.items():
        print(f"{name}: {value}")

    print("\nPLATFORM PERFORMANCE")
    print("=" * 40)

    for platform, group in df.groupby("platform"):
        print(f"\n{platform}")

        for name, value in calculate_metrics(group).items():
            print(f"{name}: {value}")


if __name__ == "__main__":
    main()
