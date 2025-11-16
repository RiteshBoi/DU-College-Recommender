import pandas as pd

# College Data (20 Colleges × 10 Branches)
colleges = [
    'DTU', 'NSIT', 'IIIT Delhi', 'IGDTUW', 'MAIT', 'MSIT', 'BVP', 'DCE', 'NIT Delhi', 'GTBIT',
    'JMI', 'USICT', 'ADGITM', 'BVCOE', 'HMRITM', 'NIEC', 'Maharaja Surajmal', 'BPIT',
    'IPU Main Campus', 'Ambedkar Institute'
]
branches = ['CSE', 'ECE', 'ME', 'EE', 'CE', 'IT', 'ICE', 'SE', 'PIE', 'ENE']

# Representative 2025 cutoffs 
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

# Create DataFrame
college_data = pd.DataFrame({
    "College": [c for c in colleges for _ in branches],
    "Branch": branches * len(colleges),
    "Cutoff_2025": cutoffs_2025
})


# Core Functions

def best_suited(percentile):
    return college_data[college_data["Cutoff_2025"] <= percentile]

def additional_options(percentile):
    return college_data[
        (college_data["Cutoff_2025"] > percentile) & 
        (college_data["Cutoff_2025"] <= percentile + 5)
    ]

def show_all_cutoffs():
    return college_data

def get_trend_data():
    data = {
        "Year": list(range(2015, 2026)),
        "Cutoff_Percentile": [82.5, 84.2, 85.1, 86.8, 88.0, 89.5, 90.2, 91.0, 92.3, 93.8, 94.6]
    }
    return pd.DataFrame(data)
