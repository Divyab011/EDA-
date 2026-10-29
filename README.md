# 🚢 Titanic Disaster: Exploratory Data Analysis & Survival Modeling
### CodeAlpha Data Analytics Internship — Task 2

![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13%2B-4c72b0?logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8%2B-11557c)
![Status](https://img.shields.io/badge/Status-Completed%20%E2%9C%85-brightgreen)
![Internship](https://img.shields.io/badge/CodeAlpha-Task%202%20Submission-orange)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📑 Table of Contents
1. [Executive Summary & Overview](#-executive-summary--overview)
2. [🚀 How to Run Everything (Quickstart)](#-how-to-run-everything-quickstart)
   - [Prerequisites](#prerequisites)
   - [Step 1: Clone or Navigate to the Repository](#step-1-clone-or-navigate-to-the-repository)
   - [Step 2: Create & Activate Virtual Environment](#step-2-create--activate-virtual-environment)
   - [Step 3: Install Required Dependencies](#step-3-install-required-dependencies)
   - [Step 4: Execute the End-to-End Pipeline](#step-4-execute-the-end-to-end-pipeline)
   - [Step 5: Launch & Run Jupyter Notebook](#step-5-launch--run-jupyter-notebook)
3. [📢 How to Post & Submit Everything](#-how-to-post--submit-everything)
   - [Part 1: How to Post on LinkedIn](#part-1-how-to-post-on-linkedin)
   - [Part 2: How to Record & Share the Video Presentation](#part-2-how-to-record--share-the-video-presentation)
   - [Part 3: How to Submit to CodeAlpha](#part-3-how-to-submit-to-codealpha)
4. [📂 Repository Structure & File Guide](#-repository-structure--file-guide)
5. [🧹 Methodology: Cleaning & Feature Engineering](#-methodology-cleaning--feature-engineering)
6. [📊 Key Findings & Visualization Highlights](#-key-findings--visualization-highlights)
7. [🔬 Statistical Hypothesis Testing](#-statistical-hypothesis-testing)
8. [💡 Strategic Business & Safety Implications](#-strategic-business--safety-implications)
9. [🛠️ Troubleshooting & FAQs](#️-troubleshooting--faqs)

---

## 📌 Executive Summary & Overview
This repository contains an end-to-end **Exploratory Data Analysis (EDA)** and survival pattern investigation on the historic Titanic passenger manifest (`train.csv`, $N = 891$), developed as **Task 2 of the CodeAlpha Data Analytics Internship**.

The objective is to combine rigorous descriptive statistics, data cleansing, feature engineering, hypothesis validation ($\chi^2$ and Mann-Whitney $U$ tests), and publication-standard visualizations to reveal how biological sex, socioeconomic class, ticket pricing, family dynamics, and cabin architecture governed passenger survival.

```
                              [Titanic Manifest: 891 Passengers]
                                              │
                 ┌────────────────────────────┴───────────────────────────┐
                 ▼                                                        ▼
         [Died: 549 (61.6%)]                                    [Survived: 342 (38.4%)]
                 │                                                        │
    ┌────────────┴────────────┐                              ┌────────────┴────────────┐
    ▼                         ▼                              ▼                         ▼
[Males: 81.1% of Men]   [3rd Class: 75.8%]           [Females: 74.2% of Women]   [1st Class: 63.0%]
```

---

## 🚀 How to Run Everything (Quickstart)

Follow these step-by-step instructions to set up the environment, run the complete automated analysis pipeline, and interact with the Jupyter Notebook.

### Prerequisites
* **Python**: Version 3.10, 3.11, or 3.12 installed on your system ([Download Python](https://www.python.org/downloads/)).
* **Git**: Installed for cloning and version control ([Download Git](https://git-scm.com/)).
* **OS**: Compatible with Windows 10/11, macOS, or Linux.

---

### Step 1: Clone or Navigate to the Repository

Open your terminal or command prompt:

```bash
# If cloning from GitHub:
git clone https://github.com/Divyab011/EDA-.git
cd EDA-

# If already in the project directory:
cd "d:\My Stuff\Data Analystics\EDA"
```

---

### Step 2: Create & Activate Virtual Environment

Isolate the project packages from your system Python:

#### On Windows (PowerShell):
```powershell
# Create virtual environment named .venv
python -m venv .venv

# If script execution is restricted, temporarily allow in current process:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activate the environment
.venv\Scripts\Activate.ps1
```

#### On Windows (Command Prompt - cmd):
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

#### On macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

> **Verification**: When activated, your prompt will show `(.venv)` at the beginning of the line.

---

### Step 3: Install Required Dependencies

Install all core analytics, statistics, and visualization packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

*Packages installed include `pandas`, `numpy`, `scipy`, `matplotlib`, `seaborn`, `jupyter`, and `notebook`.*

---

### Step 4: Execute the End-to-End Pipeline

Run the master pipeline script to process the raw dataset, execute intelligent imputations, run IQR outlier checks, and generate all 10 high-resolution figures:

```bash
python run_analysis.py
```

#### What happens during execution:
1. **Loads Data**: Reads `data/raw/train.csv` (891 rows, 12 columns).
2. **Data Integrity Inspection**: Checks data types, null counts, and duplicates.
3. **Data Cleaning & Engineering**:
   - Parses passenger social titles (`Mr`, `Mrs`, `Miss`, `Master`, `Officer`, `Royalty`).
   - Imputes missing `Age` values based on median age per `Pclass` and `Title`.
   - Extracts `Cabin` deck indicators and flags known cabins.
   - Imputes `Embarked` missing records with the mode (`S`).
   - Computes `FamilySize`, `IsAlone`, `AgeGroup`, and `FareCategory`.
4. **Exports Cleaned Dataset**: Saves clean data to `data/processed/titanic_cleaned.csv`.
5. **IQR Outlier Detection**: Identifies and quantifies outliers in `Fare` and `Age`.
6. **Generates Figures**: Renders 10 publication-quality charts (300 DPI) into `reports/figures/`.

---

### Step 5: Launch & Run Jupyter Notebook

To explore the code interactively, run the narrative-driven Jupyter notebook:

```bash
jupyter notebook notebooks/Titanic_EDA_Analysis.ipynb
```

Or open the repository in **VS Code**, open `notebooks/Titanic_EDA_Analysis.ipynb`, select the `.venv` Python kernel at the top right, and click **Run All Cells**.

---

## 📢 How to Post & Submit Everything

This section provides the exact instructions, templates, and procedures to showcase your project on **LinkedIn**, record your **video presentation**, and submit to the **CodeAlpha Internship portal**.

---

### Part 1: How to Post on LinkedIn

Posting your project demonstrates your analytical communication, business translation, and technical visualization skills.

#### 📝 Posting Steps:
1. Log in to your [LinkedIn account](https://www.linkedin.com).
2. Click **"Start a post"**.
3. Copy and paste the template below into your post editor.
4. Replace placeholder brackets (like `[Your Name]` and `[Insert your GitHub repo link]`) with your real details.
5. **Attach Visual Media**:
   - Click the **Media / Image** icon.
   - Upload `reports/figures/10_multivariate_summary_dashboard.png` (gives the strongest immediate visual impact!).
   - *Optional:* Upload 3–4 additional charts (`02_gender_vs_survival.png`, `03_pclass_vs_survival.png`, `06_family_size_survival.png`) as a multi-image carousel.
6. Tag the company: Type `@CodeAlpha` and select their official company page.
7. Click **Post**.

---

#### 📋 Ready-to-Copy LinkedIn Post Template:

```text
🚢 Uncovering the Hidden Determinants of Survival: Titanic Exploratory Data Analysis (EDA) 📊

I am pleased to share my latest data science project completed as part of the CodeAlpha Data Analytics Internship (Task 2)!

Using Python, Pandas, Matplotlib, and Seaborn, I executed an end-to-end Exploratory Data Analysis on the historic Titanic passenger manifest (N = 891) to evaluate how demographic profiles, socioeconomic class, and evacuation logistics dictated survival.

Here is what the empirical data revealed:

🔍 5 Key Analytical Insights:
1️⃣ The "Women & Children First" Protocol Held Strong:
Female passengers had a 74.20% survival rate vs. 18.89% for males (χ² = 260.71, p < 0.001). A woman was nearly 4x more likely to survive than a man.

2️⃣ The Socioeconomic Evacuation Divide:
1st Class passengers experienced a 62.96% survival rate, compared to only 24.24% for 3rd Class passengers—a 2.6x disparity directly driven by upper-deck cabin locations and rapid lifeboat access.

3️⃣ Age & Vulnerability:
Infants (0–5 years) achieved the highest survival rate across all demographics at 70.45%, while seniors (56+) faced significant vulnerability with only 30.19% surviving.

4️⃣ The Family Size "Sweet Spot":
Small family units (2–4 members) achieved the highest survival rate (57.88%), significantly outperforming solo travelers (30.35%) and large families of 5+ (16.13%), highlighting the coordination breakdown of large households during maritime crises.

5️⃣ Purchasing Power & Safety:
Survivors paid a median fare of £26.00 vs £10.50 for deceased passengers (Mann-Whitney U = 57,877, p < 0.001). Top quartile fare holders had a 58.11% survival rate vs 19.73% for the lowest quartile.

🛠️ Technical Highlights:
• Intelligent Imputation: Modeled missing Age values using grouped medians by Pclass and extracted Social Titles (Mr, Mrs, Miss, Master, Officer).
• Feature Engineering: FamilySize, IsAlone flags, Deck extraction from Cabin, and Fare quartiles.
• Statistical Hypothesis Testing: Chi-Square tests of independence and non-parametric Mann-Whitney U tests.
• Publication Visualizations: 10 clean, high-resolution charts adhering to professional visual hierarchy.

📁 GitHub Repository: [Insert your GitHub repo link here]
📓 Interactive Notebook: notebooks/Titanic_EDA_Analysis.ipynb
🎥 Video Presentation: [Insert your Loom / YouTube link here]

Thank you to CodeAlpha for this rewarding challenge! I welcome feedback and discussions in the comments. 👇

#DataAnalytics #ExploratoryDataAnalysis #Python #Pandas #Seaborn #Matplotlib #DataScience #CodeAlpha #Internship #BusinessIntelligence #Statistics #EDA #PortfolioProject #LinkedInLearning
```

---

### Part 2: How to Record & Share the Video Presentation

CodeAlpha and modern recruiters value clear verbal communication of data findings.

#### 🎥 Recording Setup:
* **Target Duration**: Exactly 1.5 to 2 minutes (~120 seconds).
* **Recommended Free Software**:
  * [Loom](https://www.loom.com/) (Recommended: records screen + webcam bubble in 1 click).
  * [OBS Studio](https://obsproject.com/) (Open-source, no watermarks).
  * [Zoom](https://zoom.us/) (Start a meeting with just yourself, share screen, turn on camera, click "Record to this computer").

#### ⏱️ Video Cue Timeline (Reference: `submission/Video_Presentation_Script.md`):

| Time | Section | Screen Visual Cue | What to Say |
| :--- | :--- | :--- | :--- |
| **0:00 – 0:15** | Hook & Intro | Webcam + README title banner | State your name, CodeAlpha Task 2, and the project goal. |
| **0:15 – 0:35** | Data Cleaning | Show code for Title-based Age imputation | Explain 77% missing Cabin and intelligent Age imputation by Title. |
| **0:35 – 0:55** | Gender & Class Divide | Split screen: Figure 02 (Gender) & Figure 03 (Class) | 74% female vs 19% male survival; 1st class 2.6x higher than 3rd class. |
| **0:55 – 1:15** | Age & Family Dynamics | Figure 04 (Age) & Figure 06 (Family Size) | Infants (70%) vs Seniors; Small family sweet spot (58%) vs Large families (16%). |
| **1:15 – 1:40** | Statistical Rigor | Figure 08 (Heatmap) & Figure 10 (Dashboard) | $\chi^2$ significance tests, fare correlation, IQR outlier handling. |
| **1:40 – 2:00** | Takeaways & Outro | Summary table in README + Webcam | Modern safety implications (SOLAS), CodeAlpha thanks, call to action. |

> 📖 **Full Word-for-Word Script**: Open [`submission/Video_Presentation_Script.md`](file:///d:/My%20Stuff/Data%20Analystics/EDA/submission/Video_Presentation_Script.md) for the exact script you can read while recording!

#### 🌐 Uploading & Sharing Your Video:
1. **Loom**: Once finished, copy the shareable link.
2. **YouTube**: Upload as **Unlisted** (or Public) and copy the video URL.
3. **Google Drive**: Upload the `.mp4` file, right-click -> **Share** -> Change general access to **"Anyone with the link can view"** -> Copy link.

---

### Part 3: How to Submit to CodeAlpha

Before submitting your internship form, verify that your deliverables are organized:

#### Pre-Submission Checklist:
- [x] Code pushed to a **Public** GitHub repository.
- [x] Cleaned dataset generated in `data/processed/titanic_cleaned.csv`.
- [x] All 10 figures rendered in `reports/figures/`.
- [x] Jupyter Notebook (`notebooks/Titanic_EDA_Analysis.ipynb`) fully executed with visible cell outputs.
- [x] LinkedIn post published and public.
- [x] 2-minute video presentation recorded and link verified.

#### Information to Enter on the CodeAlpha Submission Form:
* **Internship Track**: Data Analytics
* **Task Number**: Task 2 (Exploratory Data Analysis - EDA)
* **GitHub Repository URL**: `https://github.com/your-username/Titanic-Exploratory-Data-Analysis`
* **LinkedIn Post URL**: Click the three dots `...` on your LinkedIn post -> **Copy link to post**.
* **Video Presentation URL**: Your YouTube / Loom / Google Drive link.

---

## 📂 Repository Structure & File Guide

```bash
EDA/
├── data/
│   ├── raw/
│   │   └── train.csv                 # Raw Titanic passenger dataset (891 rows, 12 columns)
│   └── processed/
│       └── titanic_cleaned.csv        # Cleaned dataset with engineered attributes
├── notebooks/
│   └── Titanic_EDA_Analysis.ipynb    # Executed Jupyter Notebook with outputs & plots
├── src/
│   ├── __init__.py                   # Package initializer
│   ├── data_cleaning.py              # Data ingestion, inspection, imputation, and IQR detection
│   ├── eda_visualizations.py         # 10 publication-quality Seaborn/Matplotlib visualization functions
│   └── statistical_checks.py         # Hypothesis testing engine (Chi-Square & Mann-Whitney U)
├── reports/
│   ├── figures/                      # 10 generated high-resolution chart exports (300 DPI)
│   │   ├── 01_survival_countplot.png
│   │   ├── 02_gender_vs_survival.png
│   │   ├── 03_pclass_vs_survival.png
│   │   ├── 04_age_distribution_survival.png
│   │   ├── 05_fare_distribution_survival.png
│   │   ├── 06_family_size_survival.png
│   │   ├── 07_embarked_vs_survival.png
│   │   ├── 08_correlation_heatmap.png
│   │   ├── 09_boxplots_outliers.png
│   │   └── 10_multivariate_summary_dashboard.png
│   └── executive_summary.md          # Senior Data Analyst executive briefing report
├── submission/
│   ├── LinkedIn_Post.md              # Ready-to-use LinkedIn showcase template
│   └── Video_Presentation_Script.md  # 2-minute video presentation script with visual cues
├── run_analysis.py                   # Master automated runner executing pipeline end-to-end
├── build_notebook.py                 # Notebook scaffold builder
├── execute_notebook.py               # Headless automated notebook executor
├── requirements.txt                  # Python dependencies
├── pyrightconfig.json                # Python language server configuration
├── .gitignore                        # Git ignore patterns
└── README.md                         # Complete project documentation & guide
```

---

## 🧹 Methodology: Cleaning & Feature Engineering

### 1. Intelligent Missing Value Imputation
| Feature | Missing Count (%) | Handling Strategy | Analytical Rationale |
| :--- | :--- | :--- | :--- |
| `Cabin` | 687 (77.10%) | Extracted `Deck` letter & created `Cabin_Known` flag | Missingness was Not at Random (MNAR); 3rd class passengers were rarely assigned cabin numbers. |
| `Age` | 177 (19.87%) | Grouped median imputation by `Pclass` and extracted `Title` | Simple mean/median distorts age demographics. A 1st class "Master" is a child, while a 1st class "Mr" is an adult. |
| `Embarked` | 2 (0.22%) | Replaced with mode (`'S'` for Southampton) | Southampton accounted for 72.4% of all passenger departures. |

### 2. Feature Engineering
* **`Title`**: Extracted from `Name` and normalized into `Mr`, `Miss`, `Mrs`, `Master`, `Officer`, `Royalty`.
* **`FamilySize`**: Computed as `SibSp + Parch + 1` (total travel party size).
* **`IsAlone`**: Binary indicator (`1` if `FamilySize == 1`, else `0`).
* **`FamilyGroup`**: Categorized into `Alone (1)`, `Small Family (2-4)`, and `Large Family (5+)`.
* **`AgeGroup`**: Partitioned into `Infants (0-5)`, `Children (6-12)`, `Teens (13-19)`, `Young Adults (20-35)`, `Middle Aged (36-55)`, and `Seniors (56+)`.
* **`FareCategory`**: Discretized into quartiles: `Low (0-25%)`, `Medium (25-50%)`, `High (50-75%)`, and `Very High (75-100%)`.

---

## 📊 Key Findings & Visualization Highlights

| Figure | Chart Type | Key Takeaway |
| :--- | :--- | :--- |
| **01** | [Survival Countplot](reports/figures/01_survival_countplot.png) | Overall survival rate was only **38.38%** (342 survivors vs 549 fatalities) due to severe lifeboat shortages. |
| **02** | [Gender vs Survival](reports/figures/02_gender_vs_survival.png) | Women achieved **74.20%** survival vs **18.89%** for men ($\chi^2 = 260.71, p < 0.001$). Nearly **4x advantage**. |
| **03** | [Class vs Survival](reports/figures/03_pclass_vs_survival.png) | 1st Class: **62.96%**, 2nd Class: **47.28%**, 3rd Class: **24.24%**. 1st class passengers had **2.6x** higher survival. |
| **04** | [Age Distribution](reports/figures/04_age_distribution_survival.png) | Infants (0–5) had the highest survival (**70.45%**); seniors (56+) experienced lowest adult survival (**30.19%**). |
| **05** | [Fare Distribution](reports/figures/05_fare_distribution_survival.png) | Survivors paid a median of **£26.00** vs **£10.50** for non-survivors ($p = 7.42 \times 10^{-22}$). |
| **06** | [Family Size](reports/figures/06_family_size_survival.png) | **Small families (2–4)** achieved the highest survival (**57.88%**); large families collapsed to **16.13%**. |
| **07** | [Port of Embarkation](reports/figures/07_embarked_vs_survival.png) | Cherbourg had highest survival (**55.36%**), explained by 51% of Cherbourg passengers being in 1st class. |
| **08** | [Correlation Heatmap](reports/figures/08_correlation_heatmap.png) | Strongest positive predictor: female sex ($+0.54$); strongest negative predictor: `Pclass` ($-0.34$). |
| **09** | [IQR Outlier Boxplots](reports/figures/09_boxplots_outliers.png) | 116 Fare outliers detected (up to £512.33), preserved as legitimate luxury suites. |
| **10** | [Multivariate Dashboard](reports/figures/10_multivariate_summary_dashboard.png) | Unified 4-panel executive overview combining demographic and socioeconomic interactions. |

---

## 🔬 Statistical Hypothesis Testing

To ensure conclusions were statistically validated and not random noise:

1. **Sex vs Survival ($\chi^2$ Test)**:
   * Null Hypothesis: Passenger survival is independent of sex.
   * Result: $\chi^2 = 260.71, \text{df} = 1, p = 1.20 \times 10^{-58}$.
   * Decision: **Reject Null Hypothesis ($p < 0.001$)**. Strong statistical dependency.
2. **Passenger Class vs Survival ($\chi^2$ Test)**:
   * Null Hypothesis: Survival is independent of socioeconomic ticket class.
   * Result: $\chi^2 = 102.89, \text{df} = 2, p = 4.55 \times 10^{-23}$.
   * Decision: **Reject Null Hypothesis ($p < 0.001$)**. Class was a defining survival factor.
3. **Fare vs Survival (Mann-Whitney $U$ Test)**:
   * Null Hypothesis: Ticket fare distribution is equal between survivors and non-survivors.
   * Result: $U = 57,877, p = 7.42 \times 10^{-22}$.
   * Decision: **Reject Null Hypothesis ($p < 0.001$)**. Survivors paid significantly higher fares.

---

## 💡 Strategic Business & Safety Implications

1. **Vessel Architecture & Evacuation Routes**: Lower-deck passengers suffered devastating mortality due to winding corridors and closed bulkheads. Modern transit designs now incorporate direct, unobstructed vertical escape trunks.
2. **Emergency Protocol Standardization**: Boarding guidelines differed between the port side ("women and children only") and starboard side ("women and children first"). Standardized emergency checklists eliminate dangerous operator variance.
3. **Muster Station Tracking for Large Families**: Large family mortality (**83.9% died**) demonstrates that families refuse to evacuate when members are separated. Modern cruise lines utilize RFID/Bluetooth muster bracelets to verify family assemblies instantly.
4. **Regulatory Legacy**: This tragedy directly established the **1914 International Convention for the Safety of Life at Sea (SOLAS)**, requiring 100%+ lifeboat capacity, regular passenger muster drills, and 24-hour radio monitoring.

---

## 🛠️ Troubleshooting & FAQs

### Q1: When running `.venv\Scripts\Activate.ps1`, I get an execution policy error.
**Solution**: Windows PowerShell restricts script execution by default. Run this in PowerShell before activating:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
Then run `.venv\Scripts\Activate.ps1` again.

### Q2: I receive `ModuleNotFoundError: No module named 'src'`.
**Solution**: Make sure you are executing commands from the project root directory (`d:\My Stuff\Data Analystics\EDA`). `run_analysis.py` automatically injects `src` into `sys.path`.

### Q3: My Matplotlib plots do not show on screen or freeze.
**Solution**: `eda_visualizations.py` is configured with Matplotlib's headless `'Agg'` backend (`matplotlib.use('Agg')`). This prevents GUI freezes and exports crisp, 300 DPI `.png` files directly to `reports/figures/`.

### Q4: How do I open the notebook in VS Code without opening the web browser?
**Solution**:
1. Open VS Code in this directory (`code .`).
2. Open `notebooks/Titanic_EDA_Analysis.ipynb`.
3. In the upper-right corner of the notebook editor, click **Select Kernel** -> **Python Environments...** -> Choose `.venv`.
4. Click **Run All**.

---

## 👨‍💻 Project Metadata & Contact
* **Internship**: CodeAlpha Data Analytics Internship
* **Task Assigned**: Task 2 — Exploratory Data Analysis (EDA)
* **Dataset**: Titanic Passenger Manifest (`train.csv`)
* **License**: MIT Open Source

---
*Developed with rigorous data science methodologies, structured modular code, and business intelligence principles.*
