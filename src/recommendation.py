import numpy as np
import pandas as pd

from config import RAW_DATA_DIR, OUTPUT_DIR
from metrics import calculate_metrics

TOTAL_BUDGET = 1_000_000   # Rs.
MIN_SHARE = 0.05           # every platform gets at least 5%
MAX_SHARE = 0.40           # no platform gets more than 40%
WEIGHTS = {"ROAS": 0.50, "CPA": 0.25, "CVR": 0.25}
LABELS = [
    "Top priority",
    "High priority",
    "Medium priority",
    "Low priority",
    "Lowest priority",
]


def calculate_scores(platform_df):
    """Score each platform from 0 to 1 (1 = best platform on that metric)."""
    roas_score = platform_df["ROAS"] / platform_df["ROAS"].max()

    # CPA: lower is better, so invert it
    cpa = platform_df["CPA"].replace(0, np.nan)
    cpa_score = (cpa.min() / cpa).fillna(0)

    cvr = platform_df["Conversion Rate (%)"]
    cvr_score = cvr / cvr.max()

    return (
        WEIGHTS["ROAS"] * roas_score
        + WEIGHTS["CPA"] * cpa_score
        + WEIGHTS["CVR"] * cvr_score
    )


def allocate_shares(scores):
    """Turn scores into budget shares that sum to 100%,
    respecting the minimum and maximum share per platform."""
    shares = pd.Series(np.nan, index=scores.index)
    free = list(scores.index)

    while free:
        remaining = 1 - shares.dropna().sum()
        tentative = scores[free] / scores[free].sum() * remaining

        too_low = tentative[tentative < MIN_SHARE].index
        too_high = tentative[tentative > MAX_SHARE].index

        if len(too_low) == 0 and len(too_high) == 0:
            shares[free] = tentative
            break

        shares[too_low] = MIN_SHARE
        shares[too_high] = MAX_SHARE
        free = [p for p in free if p not in too_low and p not in too_high]

    return shares


def generate_recommendations():
    input_file = RAW_DATA_DIR / "marketing_data_1000000.csv"

    if not input_file.exists():
        raise FileNotFoundError(f"Dataset not found: {input_file}")

    df = pd.read_csv(input_file)

    rows = []
    for platform, group in df.groupby("platform"):
        metrics = calculate_metrics(group)
        metrics["platform"] = platform
        rows.append(metrics)

    platform_df = pd.DataFrame(rows).set_index("platform")

    scores = calculate_scores(platform_df)
    shares = allocate_shares(scores)

    amounts = (shares * TOTAL_BUDGET).round(0)
    amounts.loc[amounts.idxmax()] += TOTAL_BUDGET - amounts.sum()

    result = pd.DataFrame({
        "platform": platform_df.index,
        "ROAS": platform_df["ROAS"].values,
        "CPA": platform_df["CPA"].values,
        "CTR (%)": platform_df["CTR (%)"].values,
        "Conversion Rate (%)": platform_df["Conversion Rate (%)"].values,
        "score": scores.round(3).values,
        "current_spend_share (%)": (
            platform_df["spend"] / platform_df["spend"].sum() * 100
        ).round(1).values,
        "recommended_share (%)": (shares * 100).round(1).values,
        "recommended_budget_Rs": amounts.astype(int).values,
    })

    result["expected_revenue_Rs"] = (
        result["recommended_budget_Rs"] * result["ROAS"]
    ).round(0).astype(int)

    result = result.sort_values(
        "recommended_budget_Rs", ascending=False
    ).reset_index(drop=True)
    result["rank"] = range(1, len(result) + 1)
    result["recommendation"] = [LABELS[i] for i in range(len(result))]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / "recommendation.csv"
    result.to_csv(output_file, index=False)

    print("\nBUDGET RECOMMENDATION (Total: Rs. {:,})".format(TOTAL_BUDGET))
    print("=" * 70)
    print(result.to_string(index=False))
    print(f"\nTotal allocated: Rs. {result['recommended_budget_Rs'].sum():,}")
    print(f"Expected revenue: Rs. {result['expected_revenue_Rs'].sum():,}")
    print(f"Saved recommendation: {output_file}")


if __name__ == "__main__":
    generate_recommendations()

