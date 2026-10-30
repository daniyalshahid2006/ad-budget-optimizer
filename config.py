
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

OUTPUT_DIR = BASE_DIR / "outputs"
CHARTS_DIR = OUTPUT_DIR / "charts"
REPORT_DIR = BASE_DIR / "report"

# Reproducible data generation
RANDOM_SEED = 42

# Dataset sizes required for the project
DATASET_SIZES = [
    10_000,
    100_000,
    1_000_000,
    10_000_000,
]

# Advertising platforms
PLATFORMS = [
    "Facebook",
    "Instagram",
    "Google",
    "TikTok",
    "YouTube",
]

# Total advertising budget
TOTAL_BUDGET = 1_000_000
CURRENCY = "PKR"

# Generate large datasets in manageable chunks
CHUNK_SIZE = 1_000_000
