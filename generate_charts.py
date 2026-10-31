
import os
import pandas as pd
import matplotlib.pyplot as plt

# Project paths
INPUT_FILE = "outputs/benchmarks/benchmark_results.csv"
OUTPUT_DIR = "outputs/charts"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load existing benchmark results (no benchmark rerun)
df = pd.read_csv(INPUT_FILE)

# Ensure dataset sizes are numeric
df["dataset_size"] = df["dataset_size"].astype(int)

# Pivot benchmark data
pivot = df.pivot(
    index="dataset_size",
    columns="pipeline",
    values="average_time_seconds"
)

pivot = pivot.sort_index()

# Chart 1: Execution Time Comparison
plt.figure(figsize=(10, 6))
pivot.plot(kind="bar", figsize=(10, 6))
plt.title("Execution Time Comparison")
plt.xlabel("Dataset Size (Rows)")
plt.ylabel("Average Execution Time (Seconds)")
plt.xticks(rotation=0)
plt.legend(title="Processing Pipeline")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "execution_time_comparison.png"), dpi=300)
plt.close()

# Chart 2: Scalability Comparison
plt.figure(figsize=(10, 6))

for pipeline in pivot.columns:
    plt.plot(
        pivot.index,
        pivot[pipeline],
        marker="o",
        label=pipeline
    )

plt.title("Processing Pipeline Scalability")
plt.xlabel("Dataset Size (Rows)")
plt.ylabel("Average Execution Time (Seconds)")
plt.xscale("log")
plt.legend(title="Processing Pipeline")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "scalability_comparison.png"), dpi=300)
plt.close()

# Chart 3: Log-scale Performance Comparison
plt.figure(figsize=(10, 6))

for pipeline in pivot.columns:
    plt.plot(
        pivot.index,
        pivot[pipeline],
        marker="o",
        label=pipeline
    )

plt.title("Log-Scale Execution Time Comparison")
plt.xlabel("Dataset Size (Rows)")
plt.ylabel("Average Execution Time (Seconds)")
plt.xscale("log")
plt.yscale("log")
plt.legend(title="Processing Pipeline")
plt.grid(True, which="both")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "log_scale_comparison.png"), dpi=300)
plt.close()

print("Successfully generated 3 comparison charts!")

for filename in os.listdir(OUTPUT_DIR):
    if filename.endswith(".png"):
        print("Created:", filename)
