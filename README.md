# 🚀 Ad Budget Optimizer

### Performance Benchmarking and Advertising Analytics Using Pandas, MapReduce, and Apache Spark

The **Ad Budget Optimizer** is a Python-based data processing and analytics project that evaluates the performance of three different data processing approaches: **Pandas, MapReduce, and Apache Spark**.

The project processes synthetic advertising campaign datasets of varying sizes to compare execution performance, analyze advertising metrics, and identify the most effective advertising platform based on Return on Ad Spend (ROAS).

It evaluates advertising performance across **Facebook, Instagram, and Google**, providing data-driven recommendations to support advertising budget allocation.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Objectives](#-objectives)
- [Technologies](#-technologies-used)
- [System Architecture](#-system-architecture)
- [Dataset Information](#-dataset-information)
- [Project Structure](#-project-structure)
- [Installation](#-installation-and-setup)
- [Running the Application](#-running-the-application)
- [Benchmarking Methodology](#-benchmarking-methodology)
- [Benchmark Results](#-benchmark-results)
- [Performance Visualizations](#-performance-visualizations)
- [Advertising Analytics](#-advertising-analytics)
- [Recommendation System](#-recommendation-system)
- [Reproducibility and Data Management](#-reproducibility-and-data-management)
- [Conclusion](#-conclusion)
- [Author](#-author)

---

## 📖 Project Overview

Digital advertising platforms generate large volumes of campaign data. Analyzing this information efficiently is important for understanding advertising performance and making informed budget allocation decisions.

This project addresses two main challenges:

1. **Processing Performance:** How do different data processing technologies perform when handling increasingly large advertising datasets?
2. **Advertising Optimization:** Which advertising platform generates the highest return on advertising expenditure?

To investigate these questions, the project implements three independent processing pipelines and evaluates them using four dataset sizes.

The results are used to compare scalability, processing efficiency, and advertising platform performance.

## 🎯 Objectives

- Implement Pandas-based data processing.
- Develop a MapReduce-inspired processing pipeline.
- Implement distributed data processing using Apache Spark.
- Compare processing performance across different dataset sizes.
- Measure execution time using repeated benchmark executions.
- Calculate important advertising performance metrics.
- Generate performance comparison charts.
- Rank advertising platforms based on ROAS.
- Produce automated advertising recommendations.
- Maintain reproducible dataset generation.

---

## 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Synthetic dataset generation |
| Pandas | Data manipulation and analysis |
| MapReduce | Mapper and reducer-based processing |
| Apache Spark | Distributed data processing |
| PySpark | Python interface for Spark |
| Matplotlib | Benchmark visualization |
| Java 17 | Spark runtime requirement |

---

## 🏗 System Architecture

The application follows a modular processing architecture.

### Processing Workflow

1. **Dataset Generation:** Creates synthetic advertising datasets using a fixed random seed.
2. **Dataset Validation:** Checks whether the required datasets exist and generates missing datasets.
3. **Data Processing:** Sends each dataset through three independent processing pipelines.
4. **Metric Calculation:** Calculates advertising performance indicators.
5. **Benchmarking:** Measures execution time for the different processing approaches.
6. **Visualization:** Generates charts to compare processing performance.
7. **Recommendation:** Evaluates platform ROAS and produces ranked recommendations.

### Processing Approaches

**1. Pandas Pipeline**

Uses Pandas DataFrames to process advertising records, aggregate campaign metrics, and calculate performance indicators.

**2. MapReduce Pipeline**

Uses a mapper and reducer approach to organize advertising records by platform and aggregate their metrics.

**3. Apache Spark Pipeline**

Uses PySpark DataFrames and distributed processing operations to analyze advertising datasets.

---

## 📊 Dataset Information

The project uses synthetically generated advertising campaign data.

Four dataset sizes are used to evaluate processing performance.

| Dataset | Number of Records | Category |
|---|---:|---|
| Dataset 1 | 1,000 | Small |
| Dataset 2 | 10,000 | Medium |
| Dataset 3 | 100,000 | Large |
| Dataset 4 | 1,000,000 | Extra Large |

### Advertising Platforms

- Facebook
- Instagram
- Google

### Dataset Attributes

The advertising records include information such as:

- Advertising platform
- Impressions
- Clicks
- Conversions
- Advertising spend
- Revenue

### Reproducible Data Generation

The dataset generator uses a fixed random seed:

`RANDOM_SEED = 42`

This ensures that datasets can be regenerated consistently.

The generator also supports chunk-based generation to handle larger datasets efficiently.

---

## 📁 Project Structure

```text
ad-budget-optimizer/
│
├── src/
│   ├── benchmark.py
│   ├── config.py
│   ├── data_generator.py
│   ├── main.py
│   ├── mapreduce_pipeline.py
│   ├── metrics.py
│   ├── pandas_pipeline.py
│   ├── platform_profiles.py
│   ├── recommendation.py
│   └── spark_pipeline.py
│
├── data/
│   ├── raw/
│   │   └── marketing_data_10000.csv
│   │
│   └── processed/
│
├── outputs/
│   ├── benchmarks/
│   │   └── benchmark_results.csv
│   │
│   ├── charts/
│   │   ├── execution_time_comparison.png
│   │   ├── scalability_comparison.png
│   │   └── log_scale_comparison.png
│   │
│   └── recommendation.csv
│
├── generate_charts.py
├── README.md
└── .gitignore
```

---

## ⚙ Installation and Setup

### Prerequisites

Before running the project, ensure that the following are installed:

- Python 3.10 or later
- Java Development Kit (JDK) 17
- Git
- Windows, Linux, or macOS

### 1. Clone the Repository

```bash
git clone https://github.com/daniyalshahid2006/ad-budget-optimizer.git

cd ad-budget-optimizer
```

### 2. Create a Virtual Environment

Windows PowerShell:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install numpy pandas matplotlib pyspark
```

### 4. Configure Java 17

Apache Spark requires a compatible Java installation.

Install JDK 17 and configure the `JAVA_HOME` environment variable.

Verify the Java installation:

```powershell
java -version
```

---

## ▶ Running the Application

From the project root, execute:

```powershell
python .\src\main.py
```

The main application automatically:

1. Checks for the required datasets.
2. Generates missing datasets when necessary.
3. Executes the Pandas pipeline.
4. Executes the MapReduce pipeline.
5. Executes the Spark pipeline.
6. Processes all four dataset sizes.
7. Generates advertising platform recommendations.

Each pipeline is executed once per dataset size during normal application execution.

**Note:** Normal application execution is separate from the benchmark process.

---

## ⏱ Benchmarking Methodology

The project evaluates the three processing approaches using four different dataset sizes.

Each pipeline is executed three times for each dataset size.

### Total Benchmark Executions

| Parameter | Value |
|---|---:|
| Processing approaches | 3 |
| Dataset sizes | 4 |
| Repetitions per combination | 3 |
| Total executions | 36 |

Average execution times are calculated from the repeated benchmark runs.

This provides a consistent basis for comparing the processing approaches.

Benchmark results are stored in:

`outputs/benchmarks/benchmark_results.csv`

To execute the benchmark separately:

```powershell
python .\src\benchmark.py
```

This reruns the benchmark and updates the results file.

---

## 📈 Benchmark Results

The following table presents the verified average execution times obtained during benchmarking.

### Average Execution Time

| Dataset Size | Pandas | MapReduce | Spark |
|---|---:|---:|---:|
| 1,000 | 0.0036 s | 0.0027 s | 3.7426 s |
| 10,000 | 0.0123 s | 0.0256 s | 1.0840 s |
| 100,000 | 0.0644 s | 0.2684 s | 1.0780 s |
| 1,000,000 | 0.5281 s | 2.8575 s | 1.5831 s |

### Performance Analysis

**Small Datasets**

Pandas and MapReduce demonstrate very low execution times for smaller datasets. Spark has additional execution overhead, making it less efficient for these workloads in the measured environment.

**Medium and Large Datasets**

Pandas maintains strong performance as the dataset grows. MapReduce requires more processing time in these experiments.

**Extra-Large Dataset**

For one million records, Pandas records an average execution time of 0.5281 seconds, while Spark records 1.5831 seconds.

Spark performs better than the implemented MapReduce pipeline at this scale, although Pandas remains the fastest in the recorded benchmark.

These findings demonstrate that processing performance depends on dataset size, implementation, execution overhead, and the underlying hardware.

*All measurements represent the tested environment and are not universal performance guarantees.*

---

## 📉 Performance Visualizations

Three charts are generated from the benchmark results to make performance comparisons easier to interpret.

### 1. Execution Time Comparison

Compares the average execution times of Pandas, MapReduce, and Spark across all four dataset sizes.

![Execution Time Comparison](outputs/charts/execution_time_comparison.png)

### 2. Scalability Comparison

Visualizes how execution time changes as the dataset size increases.

![Scalability Comparison](outputs/charts/scalability_comparison.png)

### 3. Log-Scale Comparison

Uses a logarithmic scale to make differences across processing approaches and dataset sizes easier to examine.

![Log Scale Comparison](outputs/charts/log_scale_comparison.png)

### Regenerating Charts

To regenerate the visualizations using the existing benchmark results:

```powershell
python .\generate_charts.py
```

This script reads the saved benchmark CSV and does not rerun the benchmark.

---

## 📊 Advertising Analytics

The project calculates the following advertising performance metrics:

| Metric | Description |
|---|---|
| Impressions | Total number of advertisement views |
| Clicks | Total number of advertisement clicks |
| Conversions | Total number of completed conversion actions |
| Advertising Spend | Total advertising expenditure |
| Revenue | Total revenue generated |
| CTR | Click-Through Rate |
| CPC | Cost Per Click |
| CPM | Cost Per Thousand Impressions |
| Conversion Rate | Percentage of clicks resulting in conversions |
| ROAS | Return on Advertising Spend |

### Important Formulas

**Click-Through Rate (CTR)**

`CTR = (Clicks / Impressions) × 100`

**Cost Per Click (CPC)**

`CPC = Advertising Spend / Clicks`

**Cost Per Thousand Impressions (CPM)**

`CPM = (Advertising Spend / Impressions) × 1000`

**Conversion Rate**

`Conversion Rate = (Conversions / Clicks) × 100`

**Return on Advertising Spend (ROAS)**

`ROAS = Revenue / Advertising Spend`

---

## 🏆 Recommendation System

The recommendation system evaluates the advertising platforms using their calculated ROAS.

It analyzes the one-million-record advertising dataset and ranks platforms according to their return on advertising expenditure.

### Verified Recommendation Results

| Rank | Platform | ROAS | Recommendation |
|---:|---|---:|---|
| 1 | Google | 16.99 | Best performing platform |
| 2 | Instagram | 12.76 | Alternative platform |
| 3 | Facebook | 11.26 | Lower priority platform |

### Recommendation Analysis

**Google — Rank 1**

Google achieves the highest ROAS of 16.99, making it the best-performing platform in the generated dataset.

**Instagram — Rank 2**

Instagram achieves a ROAS of 12.76 and represents an alternative advertising platform.

**Facebook — Rank 3**

Facebook records a ROAS of 11.26, placing it third among the evaluated platforms.

### Final Recommendation

Based on the generated dataset, Google is the highest-performing advertising platform according to ROAS.

The recommendation system saves its results to:

`outputs/recommendation.csv`

---

## 🔄 Reproducibility and Data Management

The project is designed to support reproducible execution.

- A fixed random seed of 42 is used for dataset generation.
- Required datasets are checked before application execution.
- Missing datasets are generated automatically.
- Existing datasets are not unnecessarily regenerated.
- Dataset generation supports all four configured sizes.
- Benchmark results are stored separately from intermediate processing outputs.

### Repository Data Management

To keep the repository lightweight:

| File Category | Git Treatment |
|---|---|
| Source code | Included |
| 10,000-row sample dataset | Included |
| Other generated raw datasets | Excluded |
| Intermediate processed CSV files | Excluded |
| Benchmark results | Included |
| Recommendation results | Included |
| Performance charts | Included |
| Virtual environments | Excluded |
| Python cache files | Excluded |

Large datasets can be regenerated when needed by the application.

---

## 📝 Conclusion

The Ad Budget Optimizer demonstrates the implementation and evaluation of three different data processing approaches for advertising analytics.

Through experiments involving datasets ranging from 1,000 to 1,000,000 records, the project compares processing execution times and investigates how each approach behaves as the data volume increases.

The benchmark results show that Pandas performs particularly well in the tested environment, while Spark offers a different processing architecture with additional execution overhead. The implemented MapReduce pipeline provides a third approach for comparison.

The recommendation system further demonstrates how advertising metrics can support budget allocation decisions.

Google achieved the highest ROAS in the generated dataset, followed by Instagram and Facebook.

Overall, this project combines:

- Data engineering
- Data processing
- Performance benchmarking
- Advertising analytics
- Data visualization
- Automated recommendations

It provides a practical demonstration of data processing techniques and their application to digital advertising optimization.

---

## 👨‍💻 Author

**Daniyal Shahid**

GitHub: [@daniyalshahid2006](https://github.com/daniyalshahid2006)

**Project Repository:** [Ad Budget Optimizer](https://github.com/daniyalshahid2006/ad-budget-optimizer)
