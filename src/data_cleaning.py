import os
import pandas as pd
import numpy as np


def load_data(file_path: str = "data/raw/train.csv") -> pd.DataFrame:
    if not os.path.exists(file_path):
        for alt in ["train.csv", "data/train.csv"]:
            if os.path.exists(alt):
                file_path = alt
                break

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at {file_path}")

    return pd.read_csv(file_path)


def inspect_dataset(df: pd.DataFrame) -> dict:
    missing_counts = df.isnull().sum()
    missing_percentages = (missing_counts / len(df)) * 100
    missing_summary = pd.DataFrame({
        'Missing_Count': missing_counts,
        'Percentage': missing_percentages
    })
    missing_summary = missing_summary[missing_summary['Missing_Count'] > 0].sort_values(
        by='Missing_Count', ascending=False
    )

    return {
        'shape': df.shape,
        'duplicates': df.duplicated().sum(),
        'missing': missing_summary,
        'columns': list(df.columns),
        'dtypes': df.dtypes
    }


def clean_titanic_data(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()

    df_clean['Title'] = df_clean['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
    common_titles = ['Mr', 'Miss', 'Mrs', 'Master']
    title_mapping = {
        'Mlle': 'Miss',
        'Ms': 'Miss',
        'Mme': 'Mrs',
        'Lady': 'Royalty',
        'Countess': 'Royalty',
        'Sir': 'Royalty',
        'Jonkheer': 'Royalty',
        'Don': 'Royalty',
        'Dona': 'Royalty',
        'Dr': 'Officer',
        'Rev': 'Officer',
        'Col': 'Officer',
        'Major': 'Officer',
        'Capt': 'Officer'
    }
    df_clean['Title'] = df_clean['Title'].replace(title_mapping)
    df_clean['Title_Grouped'] = df_clean['Title'].apply(
        lambda x: x if x in common_titles else 'Special/Officer'
    )

    median_ages = df_clean.groupby(['Pclass', 'Title_Grouped'])['Age'].transform('median')
    df_clean['Age_Original'] = df_clean['Age']
    df_clean['Age'] = df_clean['Age'].fillna(median_ages)
    df_clean['Age'] = df_clean['Age'].fillna(df_clean['Age'].median())

    mode_embarked = df_clean['Embarked'].mode()[0]
    df_clean['Embarked'] = df_clean['Embarked'].fillna(mode_embarked)

    df_clean['Cabin_Known'] = df_clean['Cabin'].notnull().astype(int)
    df_clean['Deck'] = df_clean['Cabin'].apply(
        lambda x: str(x)[0].upper() if pd.notnull(x) else 'Unknown'
    )

    df_clean['FamilySize'] = df_clean['SibSp'] + df_clean['Parch'] + 1
    df_clean['IsAlone'] = (df_clean['FamilySize'] == 1).astype(int)
    
    family_bins = [0, 1, 4, 20]
    family_labels = ['Alone (1)', 'Small Family (2-4)', 'Large Family (5+)']
    df_clean['FamilyGroup'] = pd.cut(df_clean['FamilySize'], bins=family_bins, labels=family_labels)

    age_bins = [0, 5, 12, 19, 35, 55, 100]
    age_labels = ['Infants (0-5)', 'Children (6-12)', 'Teens (13-19)', 'Young Adults (20-35)', 'Middle Aged (36-55)', 'Seniors (56+)']
    df_clean['AgeGroup'] = pd.cut(df_clean['Age'], bins=age_bins, labels=age_labels, right=True)

    fare_labels = ['Low (0-25%)', 'Medium (25-50%)', 'High (50-75%)', 'Very High (75-100%)']
    df_clean['FareCategory'] = pd.qcut(df_clean['Fare'], q=4, labels=fare_labels, duplicates='drop')

    df_clean['Pclass_Name'] = df_clean['Pclass'].map({1: '1st Class', 2: '2nd Class', 3: '3rd Class'})
    df_clean['Survived_Label'] = df_clean['Survived'].map({0: 'Did Not Survive', 1: 'Survived'})
    df_clean['Embarked_Name'] = df_clean['Embarked'].map({
        'S': 'Southampton',
        'C': 'Cherbourg',
        'Q': 'Queenstown'
    })

    return df_clean


def detect_outliers_iqr(df: pd.DataFrame, column: str) -> dict:
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    pct = (len(outliers) / len(df)) * 100

    return {
        'column': column,
        'q1': q1,
        'q3': q3,
        'iqr': iqr,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,
        'outlier_count': len(outliers),
        'outlier_percentage': pct,
        'min_outlier': outliers[column].min() if len(outliers) > 0 else None,
        'max_outlier': outliers[column].max() if len(outliers) > 0 else None
    }


if __name__ == "__main__":
    raw_df = load_data()
    inspection = inspect_dataset(raw_df)
    print("Dataset shape:", inspection['shape'])
    print("Missing columns:\n", inspection['missing'])

    cleaned_df = clean_titanic_data(raw_df)
    os.makedirs("data/processed", exist_ok=True)
    cleaned_df.to_csv("data/processed/titanic_cleaned.csv", index=False)
    print("Cleaned data saved to data/processed/titanic_cleaned.csv")
