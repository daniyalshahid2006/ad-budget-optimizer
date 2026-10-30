
PLATFORM_PROFILES = {
    "Facebook": {
        "avg_cpc": 0.80,
        "avg_ctr": 0.025,
        "avg_conversion_rate": 0.045,
        "avg_cpm": 8.50,
    },

    "Instagram": {
        "avg_cpc": 1.00,
        "avg_ctr": 0.030,
        "avg_conversion_rate": 0.050,
        "avg_cpm": 10.00,
    },

    "Google": {
        "avg_cpc": 1.20,
        "avg_ctr": 0.040,
        "avg_conversion_rate": 0.060,
        "avg_cpm": 12.00,
    },
}


if __name__ == "__main__":
    print("Platform profiles loaded successfully!")

    for platform, metrics in PLATFORM_PROFILES.items():
        print(f"\n{platform}")
        for metric, value in metrics.items():
            print(f"  {metric}: {value}")
