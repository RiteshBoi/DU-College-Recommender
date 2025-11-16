import pandas as pd

# College Data (20 Colleges × 10 Branches)

colleges = [
    'DTU', 'NSIT', 'IIIT Delhi', 'IGDTUW', 'MAIT', 'MSIT', 'BVP', 'DCE', 'NIT Delhi', 'GTBIT',
    'JMI', 'USICT', 'ADGITM', 'BVCOE', 'HMRITM', 'NIEC', 'Maharaja Surajmal', 'BPIT',
    'IPU Main Campus', 'Ambedkar Institute'
]
branches = ['CSE', 'ECE', 'ME', 'EE', 'CE', 'IT', 'ICE', 'SE', 'PIE', 'ENE']

cutoffs_2025 = [
    98, 97, 96, 95, 94, 96, 95, 94, 93, 92, 97, 96, 95, 94, 93, 94, 93, 92, 91, 90, 96, 95, 94, 93,
    92, 95, 94, 93, 92, 91, 94, 93, 92, 91, 90, 92, 91, 90, 89, 88, 90, 89, 88, 87, 86, 89, 88, 87,
    86, 85, 89, 88, 87, 86, 85, 88, 87, 86, 85, 84, 91, 90, 89, 88, 87, 90, 89, 88, 87, 86, 92, 91,
    90, 89, 88, 91, 90, 89, 88, 87, 93, 92, 91, 90, 89, 92, 91, 90, 89, 88, 88, 87, 86, 85, 84, 87,
    86, 85, 84, 83, 90, 89, 88, 87, 86, 89, 88, 87, 86, 85, 91, 90, 89, 88, 87, 90, 89, 88, 87, 86,
    89, 88, 87, 86, 85, 88, 87, 86, 85, 84, 88, 87, 86, 85, 84, 87, 86, 85, 84, 83, 87, 86, 85, 84,
    83, 86, 85, 84, 83, 82, 86, 85, 84, 83, 82, 85, 84, 83, 82, 81, 89, 88, 87, 86, 85, 88, 87, 86,
    85, 84, 87, 86, 85, 84, 83, 86, 85, 84, 83, 82, 92, 91, 90, 89, 88, 91, 90, 89, 88, 87, 85, 84,
    83, 82, 81, 84, 83, 82, 81, 80
]

college_data = pd.DataFrame({
    "College": [c for c in colleges for _ in branches],
    "Branch": branches * len(colleges),
    "Cutoff_2025": cutoffs_2025
})


# Functions

def best_suited(percentile):
    """Return exact matches first; if none, return top 20 closest lower cutoffs."""
    exact = college_data[college_data["Cutoff_2025"] == percentile]
    if not exact.empty:
        return exact.head(20)
    else:
        lower = college_data[college_data["Cutoff_2025"] < percentile].copy()
        lower["Difference"] = percentile - lower["Cutoff_2025"]
        return lower.sort_values(by="Difference").head(20).drop(columns=["Difference"])

def additional_options(percentile):
    """Return top 30 colleges below user's percentile."""
    df = college_data[college_data["Cutoff_2025"] < percentile].copy()
    df["Difference"] = percentile - df["Cutoff_2025"]
    return df.sort_values(by="Difference").head(30).drop(columns=["Difference"])

def show_all_cutoffs():
    return college_data

def get_trend_data():
    data = {
        "Year": list(range(2015, 2026)),
        "Cutoff_Percentile": [82.5, 84.2, 85.1, 86.8, 88.0, 89.5, 90.2, 91.0, 92.3, 93.8, 94.6]
    }
    return pd.DataFrame(data)

