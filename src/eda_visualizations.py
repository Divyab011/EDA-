# pyright: reportMissingImports=false
import os
import matplotlib  # type: ignore
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type: ignore


def set_viz_style():
    sns.set_theme(style="whitegrid", palette="deep")
    plt.rcParams.update({
        'font.sans-serif': 'DejaVu Sans',
        'font.family': 'sans-serif',
        'figure.titlesize': 16,
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'figure.autolayout': True,
        'figure.dpi': 300
    })


def plot_survival_distribution(df: pd.DataFrame, output_dir: str = "reports/figures"):
    """Plot 1: Overall Survival Count & Rate"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Bar count plot
    palette = ['#e74c3c', '#2ecc71']
    ax1 = sns.countplot(x='Survived_Label', hue='Survived_Label', data=df, ax=axes[0],
                        palette=dict(zip(df['Survived_Label'].unique(), palette)), legend=False)
    axes[0].set_title("Passenger Count by Survival Status", fontweight='bold', pad=12)
    axes[0].set_xlabel("Survival Status")
    axes[0].set_ylabel("Passenger Count")

    total = len(df)
    for p in ax1.patches:
        height = p.get_height()
        axes[0].annotate(f'{height}\n({height/total*100:.1f}%)',
                         (p.get_x() + p.get_width() / 2., height / 2),
                         ha='center', va='center', fontsize=11, color='white', fontweight='bold')

    # Donut pie chart
    surv_counts = df['Survived'].value_counts()
    axes[1].pie(surv_counts, labels=['Did Not Survive', 'Survived'], autopct='%1.1f%%',
               startangle=140, colors=palette, explode=(0.04, 0.04),
               wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'width': 0.6},
               textprops={'fontsize': 11, 'fontweight': 'bold'})
    axes[1].set_title("Proportion of Overall Survival", fontweight='bold', pad=12)

    plt.suptitle("Titanic Disaster: Overall Passenger Survival Baseline", fontsize=16, fontweight='bold', y=1.03)
    out_path = os.path.join(output_dir, "01_survival_countplot.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out_path}")


def plot_gender_vs_survival(df: pd.DataFrame, output_dir: str = "reports/figures"):
    """Plot 2: Gender vs Survival Rate"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Count by Gender and Survival
    sns.countplot(x='Sex', hue='Survived_Label', data=df, ax=axes[0], palette=['#e74c3c', '#2ecc71'])
    axes[0].set_title("Passenger Breakdown by Gender & Survival", fontweight='bold', pad=12)
    axes[0].set_xlabel("Gender")
    axes[0].set_ylabel("Count")
    axes[0].legend(title="Outcome", frameon=True)

    # Annotate counts
    for p in axes[0].patches:
        height = p.get_height()
        if height > 0:
            axes[0].annotate(f'{int(height)}',
                             (p.get_x() + p.get_width() / 2., height + 6),
                             ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Survival Rate by Gender
    gender_rates = df.groupby('Sex')['Survived'].mean().reset_index()
    gender_rates['Rate_Pct'] = gender_rates['Survived'] * 100

    bars = sns.barplot(x='Sex', y='Rate_Pct', hue='Sex', data=gender_rates, ax=axes[1],
                        palette={'male': '#3498db', 'female': '#e84393'}, legend=False)
    axes[1].set_title("Survival Rate (%) by Gender", fontweight='bold', pad=12)
    axes[1].set_xlabel("Gender")
    axes[1].set_ylabel("Survival Rate (%)")
    axes[1].set_ylim(0, 100)

    for p in bars.patches:
        height = p.get_height()
        axes[1].annotate(f'{height:.1f}%',
                         (p.get_x() + p.get_width() / 2., height + 2),
                         ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.suptitle("Impact of Gender on Survival ('Women & Children First' Policy)", fontsize=16, fontweight='bold', y=1.03)
    out_path = os.path.join(output_dir, "02_gender_vs_survival.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out_path}")


def plot_pclass_vs_survival(df: pd.DataFrame, output_dir: str = "reports/figures"):
    """Plot 3: Passenger Class vs Survival"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Count plot
    sns.countplot(x='Pclass_Name', hue='Survived_Label', data=df, ax=axes[0],
                  palette=['#e74c3c', '#2ecc71'], order=['1st Class', '2nd Class', '3rd Class'])
    axes[0].set_title("Passenger Count by Class & Survival", fontweight='bold', pad=12)
    axes[0].set_xlabel("Passenger Ticket Class")
    axes[0].set_ylabel("Count")
    axes[0].legend(title="Outcome", frameon=True)

    # Survival rate by class
    pclass_rates = df.groupby('Pclass_Name')['Survived'].mean().loc[['1st Class', '2nd Class', '3rd Class']].reset_index()
    pclass_rates['Rate_Pct'] = pclass_rates['Survived'] * 100

    bars = sns.barplot(x='Pclass_Name', y='Rate_Pct', hue='Pclass_Name', data=pclass_rates, ax=axes[1],
                        palette={'1st Class': '#f39c12', '2nd Class': '#9b59b6', '3rd Class': '#34495e'}, legend=False)
    axes[1].set_title("Survival Rate (%) by Socioeconomic Class", fontweight='bold', pad=12)
    axes[1].set_xlabel("Passenger Ticket Class")
    axes[1].set_ylabel("Survival Rate (%)")
    axes[1].set_ylim(0, 100)

    for p in bars.patches:
        height = p.get_height()
        axes[1].annotate(f'{height:.1f}%',
                         (p.get_x() + p.get_width() / 2., height + 2),
                         ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.suptitle("Socioeconomic Hierarchy: Survival Disparity Across Ticket Classes", fontsize=16, fontweight='bold', y=1.03)
    out_path = os.path.join(output_dir, "03_pclass_vs_survival.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out_path}")


def plot_age_distribution_survival(df: pd.DataFrame, output_dir: str = "reports/figures"):
    """Plot 4: Age Distribution & Age Groups vs Survival"""
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # KDE distribution by survival
    sns.kdeplot(data=df[df['Survived'] == 1]['Age'], label='Survived', fill=True, color='#2ecc71', alpha=0.4, ax=axes[0], bw_adjust=0.8)
    sns.kdeplot(data=df[df['Survived'] == 0]['Age'], label='Did Not Survive', fill=True, color='#e74c3c', alpha=0.4, ax=axes[0], bw_adjust=0.8)
    axes[0].set_title("Age Density Distribution by Survival", fontweight='bold', pad=12)
    axes[0].set_xlabel("Age (Years)")
    axes[0].set_ylabel("Probability Density")
    axes[0].legend(title="Outcome", frameon=True)

    # Survival rate by age groups
    age_order = ['Infants (0-5)', 'Children (6-12)', 'Teens (13-19)', 'Young Adults (20-35)', 'Middle Aged (36-55)', 'Seniors (56+)']
    age_group_rates = df.groupby('AgeGroup', observed=False)['Survived'].mean().reindex(age_order).reset_index()
    age_group_rates['Rate_Pct'] = age_group_rates['Survived'] * 100

    bars = sns.barplot(x='AgeGroup', y='Rate_Pct', hue='AgeGroup', data=age_group_rates, ax=axes[1],
                        palette='Blues_r', legend=False)
    axes[1].set_title("Survival Rate (%) Across Demographic Age Groups", fontweight='bold', pad=12)
    axes[1].set_xlabel("Demographic Age Group")
    axes[1].set_ylabel("Survival Rate (%)")
    axes[1].tick_params(axis='x', rotation=25)
    axes[1].set_ylim(0, 100)

    for p in bars.patches:
        height = p.get_height()
        if not np.isnan(height):
            axes[1].annotate(f'{height:.1f}%',
                             (p.get_x() + p.get_width() / 2., height + 2),
                             ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.suptitle("Age Demographic Analysis: Protection of Children & Infant Survival", fontsize=16, fontweight='bold', y=1.03)
    out_path = os.path.join(output_dir, "04_age_distribution_survival.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out_path}")


def plot_fare_distribution_survival(df: pd.DataFrame, output_dir: str = "reports/figures"):
    """Plot 5: Fare Distribution & Survival by Fare Tiers"""
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Log Fare Distribution
    df['Log_Fare'] = np.log1p(df['Fare'])
    sns.histplot(data=df, x='Log_Fare', hue='Survived_Label', kde=True,
                 palette=['#e74c3c', '#2ecc71'], ax=axes[0], element='step', alpha=0.5)
    axes[0].set_title("Distribution of Log(Fare + 1) by Survival", fontweight='bold', pad=12)
    axes[0].set_xlabel("Log(Fare + 1)")
    axes[0].set_ylabel("Passenger Frequency")

    # Fare quartile survival rates
    fare_tier_order = ['Low (0-25%)', 'Medium (25-50%)', 'High (50-75%)', 'Very High (75-100%)']
    fare_rates = df.groupby('FareCategory', observed=False)['Survived'].mean().reindex(fare_tier_order).reset_index()
    fare_rates['Rate_Pct'] = fare_rates['Survived'] * 100

    bars = sns.barplot(x='FareCategory', y='Rate_Pct', hue='FareCategory', data=fare_rates, ax=axes[1],
                        palette='Purples', legend=False)
    axes[1].set_title("Survival Rate (%) by Fare Spending Quartiles", fontweight='bold', pad=12)
    axes[1].set_xlabel("Fare Quartile Tier")
    axes[1].set_ylabel("Survival Rate (%)")
    axes[1].set_ylim(0, 100)

    for p in bars.patches:
        height = p.get_height()
        axes[1].annotate(f'{height:.1f}%',
                         (p.get_x() + p.get_width() / 2., height + 2),
                         ha='center', va='bottom', fontsize=11, fontweight='bold')

    plt.suptitle("Ticket Fare Correlation: Financial Investment vs Life Safety Outcome", fontsize=16, fontweight='bold', y=1.03)
    out_path = os.path.join(output_dir, "05_fare_distribution_survival.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out_path}")


def plot_family_dynamics(df: pd.DataFrame, output_dir: str = "reports/figures"):
    """Plot 6: Family Size & Alone Status vs Survival"""
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Family Size vs Survival Rate
    fam_rate = df.groupby('FamilySize')['Survived'].mean().reset_index()
    fam_rate['Rate_Pct'] = fam_rate['Survived'] * 100

    sns.barplot(x='FamilySize', y='Rate_Pct', hue='FamilySize', data=fam_rate, ax=axes[0],
                palette='viridis', legend=False)
    axes[0].set_title("Survival Rate (%) by Total Family Size", fontweight='bold', pad=12)
    axes[0].set_xlabel("Family Size (SibSp + Parch + 1)")
    axes[0].set_ylabel("Survival Rate (%)")
    axes[0].set_ylim(0, 100)
    for p in axes[0].patches:
        h = p.get_height()
        if h > 0:
            axes[0].annotate(f'{h:.0f}%', (p.get_x() + p.get_width() / 2., h + 2),
                             ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Solo Travel vs Family Groups
    fam_group_rates = df.groupby('FamilyGroup', observed=False)['Survived'].mean().reset_index()
    fam_group_rates['Rate_Pct'] = fam_group_rates['Survived'] * 100

    bars = sns.barplot(x='FamilyGroup', y='Rate_Pct', hue='FamilyGroup', data=fam_group_rates, ax=axes[1],
                        palette='coolwarm', legend=False)
    axes[1].set_title("Survival Rate: Traveling Alone vs Small Family vs Large Family", fontweight='bold', pad=12)
    axes[1].set_xlabel("Family Group Category")
    axes[1].set_ylabel("Survival Rate (%)")
    axes[1].set_ylim(0, 100)
    for p in bars.patches:
        h = p.get_height()
        axes[1].annotate(f'{h:.1f}%', (p.get_x() + p.get_width() / 2., h + 2),
                         ha='center', va='bottom', fontsize=11, fontweight='bold')

    plt.suptitle("Family Dynamics: The Sweet Spot of Small Families (2-4 Members)", fontsize=16, fontweight='bold', y=1.03)
    out_path = os.path.join(output_dir, "06_family_size_survival.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out_path}")


def plot_embarked_vs_survival(df: pd.DataFrame, output_dir: str = "reports/figures"):
    """Plot 7: Embarkation Port vs Survival & Class Composition"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Survival Rate by Port
    emb_rate = df.groupby('Embarked_Name')['Survived'].mean().reset_index()
    emb_rate['Rate_Pct'] = emb_rate['Survived'] * 100
    sns.barplot(x='Embarked_Name', y='Rate_Pct', hue='Embarked_Name', data=emb_rate, ax=axes[0],
                palette='crest', legend=False)
    axes[0].set_title("Survival Rate (%) by Port of Embarkation", fontweight='bold', pad=12)
    axes[0].set_xlabel("Embarkation Port")
    axes[0].set_ylabel("Survival Rate (%)")
    axes[0].set_ylim(0, 100)
    for p in axes[0].patches:
        h = p.get_height()
        axes[0].annotate(f'{h:.1f}%', (p.get_x() + p.get_width() / 2., h + 2),
                         ha='center', va='bottom', fontsize=11, fontweight='bold')

    # Class Composition by Port
    class_port = pd.crosstab(df['Embarked_Name'], df['Pclass_Name'], normalize='index') * 100
    class_port[['1st Class', '2nd Class', '3rd Class']].plot(
        kind='bar', stacked=True, ax=axes[1], color=['#f39c12', '#9b59b6', '#34495e'], edgecolor='white'
    )
    axes[1].set_title("Ticket Class Composition by Port (%)", fontweight='bold', pad=12)
    axes[1].set_xlabel("Embarkation Port")
    axes[1].set_ylabel("Percentage (%)")
    axes[1].tick_params(axis='x', rotation=0)
    axes[1].legend(title="Class", frameon=True)

    plt.suptitle("Embarkation Anomaly Explained: Why Cherbourg Passengers Survived More", fontsize=16, fontweight='bold', y=1.03)
    out_path = os.path.join(output_dir, "07_embarked_vs_survival.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out_path}")


def plot_correlation_heatmap(df: pd.DataFrame, output_dir: str = "reports/figures"):
    """Plot 8: Correlation Matrix Heatmap"""
    plt.figure(figsize=(10, 8))

    # Create dummy encodings for relevant features
    df_corr = df.copy()
    df_corr['Sex_Code'] = df_corr['Sex'].map({'male': 0, 'female': 1})
    df_corr['Embarked_C'] = (df_corr['Embarked'] == 'C').astype(int)
    df_corr['Embarked_Q'] = (df_corr['Embarked'] == 'Q').astype(int)
    df_corr['Embarked_S'] = (df_corr['Embarked'] == 'S').astype(int)

    features = [
        'Survived', 'Pclass', 'Sex_Code', 'Age', 'SibSp', 'Parch',
        'Fare', 'FamilySize', 'IsAlone', 'Cabin_Known'
    ]
    corr_matrix = df_corr[features].corr()

    # Mask for upper triangle
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    sns.heatmap(corr_matrix, mask=mask, cmap='coolwarm', vmin=-0.6, vmax=0.6,
                annot=True, fmt='.2f', square=True, linewidths=1.5, cbar_kws={"shrink": .8})
    plt.title("Correlation Matrix Heatmap of Titanic Features", fontsize=16, fontweight='bold', pad=15)

    out_path = os.path.join(output_dir, "08_correlation_heatmap.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out_path}")


def plot_boxplots_outliers(df: pd.DataFrame, output_dir: str = "reports/figures"):
    """Plot 9: Boxplots for Outlier Detection in Age and Fare"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Age boxplot
    sns.boxplot(x='Survived_Label', y='Age', hue='Survived_Label', data=df, ax=axes[0],
                palette={'Did Not Survive': '#e74c3c', 'Survived': '#2ecc71'}, width=0.5, legend=False)
    axes[0].set_title("Age Distribution & Outliers by Survival", fontweight='bold', pad=12)
    axes[0].set_xlabel("Survival Status")
    axes[0].set_ylabel("Age (Years)")

    # Fare boxplot
    sns.boxplot(x='Survived_Label', y='Fare', hue='Survived_Label', data=df, ax=axes[1],
                palette={'Did Not Survive': '#e74c3c', 'Survived': '#2ecc71'}, width=0.5, legend=False)
    axes[1].set_title("Fare Distribution & High-Value Outliers", fontweight='bold', pad=12)
    axes[1].set_xlabel("Survival Status")
    axes[1].set_ylabel("Ticket Fare (£)")

    # Annotate extreme fare outlier
    max_fare = df['Fare'].max()
    axes[1].annotate(f'Top Outliers: £{max_fare:.1f}\n(Cardeza/Fortune Luxury Suites)',
                     xy=(1, max_fare), xytext=(0.4, max_fare - 80),
                     arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=6),
                     fontsize=10, fontweight='bold')

    plt.suptitle("Outlier Analysis: Identifying Statistical Anomalies in Continuous Variables", fontsize=16, fontweight='bold', y=1.03)
    out_path = os.path.join(output_dir, "09_boxplots_outliers.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out_path}")


def plot_multivariate_dashboard(df: pd.DataFrame, output_dir: str = "reports/figures"):
    """Plot 10: Multi-panel Executive Summary Dashboard"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.25)

    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])

    # 1. Gender + Class Interaction
    sns.barplot(x='Pclass_Name', y='Survived', hue='Sex', data=df, ax=ax1,
                palette=['#3498db', '#e84393'], order=['1st Class', '2nd Class', '3rd Class'])
    ax1.set_title("Survival Rate: Gender x Passenger Class", fontweight='bold')
    ax1.set_xlabel("Passenger Class")
    ax1.set_ylabel("Survival Rate")
    ax1.set_ylim(0, 1.05)
    ax1.legend(title="Gender", frameon=True)

    # 2. Fare vs Age Scatter with Survival hue
    scatter = sns.scatterplot(x='Age', y='Fare', hue='Survived_Label', data=df, ax=ax2,
                             palette=['#e74c3c', '#2ecc71'], alpha=0.7, s=50)
    ax2.set_title("Fare vs Age Distribution by Survival Outcome", fontweight='bold')
    ax2.set_xlabel("Age")
    ax2.set_ylabel("Ticket Fare (£)")
    ax2.legend(title="Outcome", frameon=True)

    # 3. Cabin Known vs Unknown
    cabin_rate = df.groupby('Cabin_Known')['Survived'].mean().reset_index()
    cabin_rate['Cabin_Label'] = cabin_rate['Cabin_Known'].map({0: 'Cabin Unknown (687)', 1: 'Cabin Recorded (204)'})
    sns.barplot(x='Cabin_Label', y='Survived', hue='Cabin_Label', data=cabin_rate, ax=ax3,
                palette={'Cabin Unknown (687)': '#7f8c8d', 'Cabin Recorded (204)': '#f1c40f'}, legend=False)
    ax3.set_title("Survival Rate: Cabin Record Availability", fontweight='bold')
    ax3.set_xlabel("Cabin Record Status")
    ax3.set_ylabel("Survival Rate")
    ax3.set_ylim(0, 1.05)
    for p in ax3.patches:
        h = p.get_height()
        ax3.annotate(f'{h*100:.1f}%', (p.get_x() + p.get_width() / 2., h + 0.03),
                     ha='center', va='bottom', fontsize=11, fontweight='bold')

    # 4. Title Grouped Survival
    title_rate = df.groupby('Title_Grouped')['Survived'].mean().sort_values(ascending=False).reset_index()
    sns.barplot(x='Title_Grouped', y='Survived', hue='Title_Grouped', data=title_rate, ax=ax4,
                palette='rocket', legend=False)
    ax4.set_title("Survival Rate by Passenger Social Title", fontweight='bold')
    ax4.set_xlabel("Extracted Title Group")
    ax4.set_ylabel("Survival Rate")
    ax4.set_ylim(0, 1.05)
    for p in ax4.patches:
        h = p.get_height()
        ax4.annotate(f'{h*100:.1f}%', (p.get_x() + p.get_width() / 2., h + 0.03),
                     ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.suptitle("CodeAlpha Task 2: Titanic Exploratory Data Analysis - Executive Dashboard",
                 fontsize=18, fontweight='bold', y=0.98)

    out_path = os.path.join(output_dir, "10_multivariate_summary_dashboard.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out_path}")


def generate_all_visualizations(df: pd.DataFrame, output_dir: str = "reports/figures"):
    """Orchestrates generation of all 10 project visualization figures."""
    os.makedirs(output_dir, exist_ok=True)
    set_viz_style()
    print("Generating all 10 high-resolution visualizations...")
    plot_survival_distribution(df, output_dir)
    plot_gender_vs_survival(df, output_dir)
    plot_pclass_vs_survival(df, output_dir)
    plot_age_distribution_survival(df, output_dir)
    plot_fare_distribution_survival(df, output_dir)
    plot_family_dynamics(df, output_dir)
    plot_embarked_vs_survival(df, output_dir)
    plot_correlation_heatmap(df, output_dir)
    plot_boxplots_outliers(df, output_dir)
    plot_multivariate_dashboard(df, output_dir)
    print("All visualizations generated successfully in:", output_dir)


if __name__ == "__main__":
    try:
        from src.data_cleaning import load_data, clean_titanic_data
    except ModuleNotFoundError:
        from data_cleaning import load_data, clean_titanic_data
    df = clean_titanic_data(load_data())
    generate_all_visualizations(df)
