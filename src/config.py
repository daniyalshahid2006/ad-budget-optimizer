
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Output directories
OUTPUT_DIR = BASE_DIR / "outputs"
BENCHMARK_DIR = OUTPUT_DIR / "benchmarks"
CHART_DIR = OUTPUT_DIR / "charts"
REPORT_DIR = BASE_DIR / "reports"

# Dataset sizes for performance testing
DATASET_SIZES = [1_000, 10_000, 100_000, 1_000_000]

# Advertising platforms
PLATFORMS = ["Facebook", "Instagram", "Google"]

# Reproducibility
RANDOM_SEED = 42

# Benchmark settings
BENCHMARK_RUNS = 3

# Ensure directories exist
for directory in [
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    BENCHMARK_DIR,
    CHART_DIR,
    REPORT_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)

print("Project configuration loaded successfully!")
print(f"Dataset sizes: {DATASET_SIZES}")
print(f"Platforms: {PLATFORMS}")
