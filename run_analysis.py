import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.data_cleaning import load_data, inspect_dataset, clean_titanic_data, detect_outliers_iqr
from src.eda_visualizations import generate_all_visualizations


def main():
    print("Running Titanic EDA Pipeline...")

    raw_df = load_data("data/raw/train.csv")

    inspection = inspect_dataset(raw_df)
    print(f"Dataset shape: {inspection['shape']}")
    print(f"Duplicates: {inspection['duplicates']}")
    print("Missing values summary:")
    print(inspection['missing'])

    cleaned_df = clean_titanic_data(raw_df)

    os.makedirs("data/processed", exist_ok=True)
    cleaned_df.to_csv("data/processed/titanic_cleaned.csv", index=False)
    print("Saved cleaned data to data/processed/titanic_cleaned.csv")

    for col in ['Fare', 'Age']:
        outlier_res = detect_outliers_iqr(cleaned_df, col)
        print(f"{col} - IQR: {outlier_res['iqr']:.2f}, Outliers: {outlier_res['outlier_count']} ({outlier_res['outlier_percentage']:.2f}%)")

    generate_all_visualizations(cleaned_df, output_dir="reports/figures")
    print("All visualizations generated in reports/figures/")


if __name__ == "__main__":
    main()
