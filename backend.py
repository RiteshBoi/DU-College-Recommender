import pandas as pd

TOTAL_CANDIDATES = 1475000  # JEE 2025 approx

def rank_to_percentile(rank):
    if pd.isna(rank) or rank <= 0:
        return 0.0
    return round(100 - (rank / TOTAL_CANDIDATES * 100), 2)

# Load CSV
df = pd.read_csv("JEE.csv")   

# Convert closing ranks to percentiles
df['Cutoff_2025'] = df['Closing_Rank'].apply(rank_to_percentile)

college_data = df[['College', 'Branch', 'Cutoff_2025']]

def best_suited(percentile):
    lower = college_data[college_data['Cutoff_2025'] < percentile].copy()
    lower['diff'] = percentile - lower['Cutoff_2025']
    return lower.sort_values(by='diff').head(30).drop(columns=['diff'])

def show_all_cutoffs():
    return college_data

def get_trend_data():
    data = {
        "Year": list(range(2015, 2026)),
        "Cutoff_Percentile": [82.5, 84.2, 85.1, 86.8, 88.0, 89.5, 90.2, 91.0, 92.3, 93.8, 94.6]
    }
    return pd.DataFrame(data)

