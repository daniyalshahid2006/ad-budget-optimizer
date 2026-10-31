import pandas as pd

from config import RAW_DATA_DIR, OUTPUT_DIR
from metrics import calculate_metrics


def analyze_campaigns():
    input_file = RAW_DATA_DIR / "marketing_data_1000000.csv"

    if not input_file.exists():
        raise FileNotFoundError(f"Dataset not found: {input_file}")

    df = pd.read_csv(input_file)

    rows = []
    for campaign_id, group in df.groupby("campaign_id"):
        metrics = calculate_metrics(group)
        metrics["campaign_id"] = campaign_id
        metrics["profit"] = round(metrics["revenue"] - metrics["spend"], 2)
        rows.append(metrics)

    result = pd.DataFrame(rows)
    result = result.sort_values("ROAS", ascending=False).reset_index(drop=True)
    result["rank"] = range(1, len(result) + 1)

    columns = [
        "rank", "campaign_id", "impressions", "clicks", "conversions",
        "spend", "revenue", "profit", "CTR (%)", "CPC", "CPA",
        "Conversion Rate (%)", "ROAS",
    ]
    result = result[columns]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / "campaign_performance.csv"
    result.to_csv(output_file, index=False)

    show = ["rank", "campaign_id", "spend", "revenue", "profit", "CPA", "ROAS"]
    print(f"\nCAMPAIGN PERFORMANCE ({len(result)} campaigns, ranked by ROAS)")
    print("=" * 70)
    print("Top 5 campaigns")
    print(result[show].head(5).to_string(index=False))
    print("\nBottom 5 campaigns")
    print(result[show].tail(5).to_string(index=False))
    print(f"\nSaved campaign performance: {output_file}")


if __name__ == "__main__":
    analyze_campaigns()
