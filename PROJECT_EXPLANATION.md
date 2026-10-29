# Titanic Exploratory Data Analysis (EDA) — Project Explanation & Guide

## 1. Project Overview

This project performs an end-to-end **Exploratory Data Analysis (EDA)** on the classic Titanic passenger manifest dataset (`train.csv`). The objective is to analyze historical passenger demographic and ticketing data to uncover patterns and factors that influenced survival during the maritime disaster.

The pipeline covers:
- Data inspection and data quality assessment
- Missing value imputation and data cleaning
- Domain-driven feature engineering
- Outlier detection using Interquartile Range (IQR)
- Statistical visual analysis using Matplotlib and Seaborn
- Modular, production-ready Python architecture and interactive Jupyter notebook exploration

---

## 2. Repository Structure

```text
EDA/
├── data/
│   ├── raw/
│   │   └── train.csv                 # Raw historical Titanic passenger dataset
│   └── processed/
│       └── titanic_cleaned.csv       # Cleaned dataset with engineered features
├── notebooks/
│   └── Titanic_EDA_Analysis.ipynb    # Interactive notebook with detailed analysis
├── reports/
│   └── figures/                      # High-resolution generated charts (PNG)
│       ├── 01_survival_countplot.png
│       ├── 02_gender_vs_survival.png
│       ├── 03_pclass_vs_survival.png
│       ├── 04_age_distribution_survival.png
│       ├── 05_fare_distribution_survival.png
│       ├── 06_family_size_survival.png
│       ├── 07_embarked_vs_survival.png
│       ├── 08_correlation_heatmap.png
│       ├── 09_boxplots_outliers.png
│       └── 10_multivariate_summary_dashboard.png
├── src/
│   ├── __init__.py                   # Package initializer
│   ├── data_cleaning.py              # Cleaning, imputation, feature engineering & IQR
│   └── eda_visualizations.py         # Visualizations generator (Seaborn & Matplotlib)
├── .gitignore                        # Git exclusion rules (venv, checkpoints, cache)
├── requirements.txt                  # Project dependencies
├── run_analysis.py                   # Master entrypoint script to run the full pipeline
├── README.md                         # Main repository README
└── PROJECT_EXPLANATION.md            # Detailed project explanation and guide (this file)
```

---

## 3. How the Pipeline Works

The entire workflow can be executed with a single command (`python run_analysis.py`). Here is what happens under the hood:

### Step 1: Data Ingestion (`src/data_cleaning.py` -> `load_data`)
- Reads the raw dataset from `data/raw/train.csv` (891 passenger records across 12 features).
- Includes fallback logic to find `train.csv` if run from different working directories.

### Step 2: Data Inspection (`src/data_cleaning.py` -> `inspect_dataset`)
- Calculates dataset dimensions (891 rows, 12 columns).
- Checks for duplicate passenger records (0 found).
- Summarizes missing values:
  - `Cabin`: 687 missing (~77.1%)
  - `Age`: 177 missing (~19.9%)
  - `Embarked`: 2 missing (~0.22%)

### Step 3: Cleaning & Feature Engineering (`src/data_cleaning.py` -> `clean_titanic_data`)
- **Title Extraction**: Extracts social titles (`Mr`, `Miss`, `Mrs`, `Master`, `Dr`, etc.) from passenger names via regex and consolidates rare titles into `Royalty` and `Officer`.
- **Targeted Age Imputation**: Instead of using a simple global mean/median, missing `Age` values are imputed using the **median age grouped by Passenger Class (`Pclass`) and Title**, preserving age-demographic distribution.
- **Port Imputation**: Missing `Embarked` values are filled with the mode (`'S'` for Southampton).
- **Cabin Deck Extraction**: Extracts deck letters (A through G) and creates a binary indicator `Cabin_Known` (1 if cabin was recorded, 0 otherwise).
- **Family Dynamics**:
  - `FamilySize` = `SibSp` + `Parch` + 1
  - `IsAlone` = 1 if traveling solo, 0 if with family
  - `FamilyGroup`: Binned into `Alone (1)`, `Small Family (2-4)`, and `Large Family (5+)`.
- **Demographic Bins**:
  - `AgeGroup`: Categorized into Infants (0-5), Children (6-12), Teens (13-19), Young Adults (20-35), Middle Aged (36-55), Seniors (56+).
  - `FareCategory`: Categorized into quartiles (`Low`, `Medium`, `High`, `Very High`).
- Saves the clean, enriched dataset to `data/processed/titanic_cleaned.csv`.

### Step 4: Outlier Detection (`src/data_cleaning.py` -> `detect_outliers_iqr`)
- Uses the standard Interquartile Range method ($IQR = Q_3 - Q_1$, boundaries $[Q_1 - 1.5 \times IQR, Q_3 + 1.5 \times IQR]$) to identify statistical outliers in `Fare` and `Age`.

### Step 5: Visualizations Generation (`src/eda_visualizations.py` -> `generate_all_visualizations`)
- Uses headless Matplotlib (`Agg`) and Seaborn to output 10 high-resolution charts saved into `reports/figures/`:
  1. `01_survival_countplot.png`: Baseline survival breakdown (38.4% survived, 61.6% perished).
  2. `02_gender_vs_survival.png`: Survival comparison by sex (Female: 74.2%, Male: 18.9%).
  3. `03_pclass_vs_survival.png`: Socioeconomic class gradient (1st: 63.0%, 2nd: 47.3%, 3rd: 24.2%).
  4. `04_age_distribution_survival.png`: Age probability density and age group survival rates.
  5. `05_fare_distribution_survival.png`: Log-transformed fare distribution and quartile survival rates.
  6. `06_family_size_survival.png`: Family size curve showing higher survival for 2-4 members.
  7. `07_embarked_vs_survival.png`: Port of embarkation survival rates and ticket class breakdown.
  8. `08_correlation_heatmap.png`: Masked correlation matrix across key numerical and encoded features.
  9. `09_boxplots_outliers.png`: Box plots showing outlier distributions for Age and Fare.
  10. `10_multivariate_summary_dashboard.png`: 4-panel executive dashboard summarizing multi-feature interactions.

---

## 4. Key Analytical Insights

1. **Gender Was the Strongest Determinant**: Females had an overall survival rate of **74.2%** compared to only **18.9%** for males, strongly validating the historical "women and children first" maritime evacuation protocol.
2. **Socioeconomic Advantage (Class & Fare)**: 1st class passengers survived at **63.0%**, compared to **47.3%** in 2nd class and only **24.2%** in 3rd class. Higher fare spending strongly correlated with higher survival rates.
3. **Age & Child Prioritization**: Infants (0-5 years) had a survival rate of ~70.5%, significantly higher than adults.
4. **Optimal Family Size**: Traveling with small families (2 to 4 members) had the highest survival rate (~57.9%). Solo travelers survived at only ~30.4%, while large families (5+ members) faced steep coordination challenges during evacuation and had the lowest survival rate (~16.1%).
5. **The Cherbourg Anomaly**: Passengers embarking at Cherbourg had a notably higher survival rate (~55.4%) compared to Southampton (~33.7%) and Queenstown (~38.9%). Cross-tabulation revealed that Cherbourg had a much higher proportion of 1st-class ticket holders (~51%).

---

## 5. How to Run the Project

### Prerequisites
- Python 3.10+ installed
- Git installed

### Setup & Execution Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Divyab011/EDA-.git
   cd EDA-
   ```

2. **Create and activate a virtual environment**:
   - On Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - On Linux/macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the master analysis pipeline**:
   ```bash
   python run_analysis.py
   ```
   This will process the raw data, generate the cleaned CSV in `data/processed/`, and export all figures to `reports/figures/`.

5. **Run the Jupyter Notebook (optional)**:
   ```bash
   jupyter notebook notebooks/Titanic_EDA_Analysis.ipynb
   ```

---

## 6. Codebase Architecture & Best Practices

- **Modularity**: Data preprocessing routines (`src/data_cleaning.py`) and visual plotting routines (`src/eda_visualizations.py`) are strictly decoupled.
- **Reproducibility**: Explicit random seeds, standardized color palettes, and deterministic grouping logic ensure reproducible outcomes.
- **Clean Code**: Written cleanly and idiomatically without unnecessary boilerplate or AI artifacts.
