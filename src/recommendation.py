
import pandas as pd
from pathlib import Path

from config import RAW_DATA_DIR, OUTPUT_DIR
from metrics import calculate_metrics


def generate_recommendations():
    input_file = RAW_DATA_DIR / "marketing_data_1000000.csv"

    if not input_file.exists():
        raise FileNotFoundError(
            f"Dataset not found: {input_file}"
        )

    df = pd.read_csv(input_file)

    results = []

    for platform, group in df.groupby("platform"):
        metrics = calculate_metrics(group)

        results.append({
            "platform": platform,
            "impressions": metrics["impressions"],
            "clicks": metrics["clicks"],
            "conversions": metrics["conversions"],
            "spend": metrics["spend"],
            "revenue": metrics["revenue"],
            "CTR (%)": metrics["CTR (%)"],
            "CPC": metrics["CPC"],
            "Conversion Rate (%)": metrics["Conversion Rate (%)"],
            "ROAS": metrics["ROAS"],
        })

    recommendations = pd.DataFrame(results)

    recommendations = recommendations.sort_values(
        by="ROAS",
        ascending=False
    )

    recommendations["rank"] = range(1, len(recommendations) + 1)

    recommendations["recommendation"] = recommendations["rank"].map({
        1: "Best performing platform",
        2: "Alternative platform",
        3: "Lower priority platform"
    })

    output_file = OUTPUT_DIR / "recommendation.csv"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    recommendations.to_csv(output_file, index=False)

    print("\nPLATFORM RECOMMENDATIONS")
    print("=" * 60)
    print(recommendations.to_string(index=False))
    print(f"\nSaved recommendation: {output_file}")


if __name__ == "__main__":
    generate_recommendations()
