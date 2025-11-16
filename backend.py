import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 20 Delhi Colleges × 10 Branches (Fixed Dataset)

college_data = {
    "College": (
        ['DTU'] * 10 +
        ['NSIT'] * 10 +
        ['IIIT Delhi'] * 10 +
        ['IGDTUW'] * 10 +
        ['MAIT'] * 10 +
        ['MSIT'] * 10 +
        ['BVP'] * 10 +
        ['DCE'] * 10 +
        ['NIT Delhi'] * 10 +
        ['GTBIT'] * 10 +
        ['JMI'] * 10 +
        ['USICT'] * 10 +
        ['ADGITM'] * 10 +
        ['BVCOE'] * 10 +
        ['HMRITM'] * 10 +
        ['NIEC'] * 10 +
        ['Maharaja Surajmal'] * 10 +
        ['BPIT'] * 10 +
        ['IPU Main Campus'] * 10 +
        ['Ambedkar Institute'] * 10
    ),

    "Branch": (
        ['CSE', 'ECE', 'ME', 'EE', 'CE', 'IT', 'ICE', 'SE', 'PIE', 'ENE'] * 20
    ),

    "Cutoff_2025": [
        98, 97, 96, 95, 94, 96, 95, 94, 93, 92,        # DTU
        97, 96, 95, 94, 93, 94, 93, 92, 91, 90,        # NSIT
        96, 95, 94, 93, 92, 95, 94, 93, 92, 91,        # IIIT Delhi
        94, 93, 92, 91, 90, 92, 91, 90, 89, 88,        # IGDTUW
        90, 89, 88, 87, 86, 89, 88, 87, 86, 85,        # MAIT
        89, 88, 87, 86, 85, 88, 87, 86, 85, 84,        # MSIT
        91, 90, 89, 88, 87, 90, 89, 88, 87, 86,        # BVP
        92, 91, 90, 89, 88, 91, 90, 89, 88, 87,        # DCE
        93, 92, 91, 90, 89, 92, 91, 90, 89, 88,        # NIT Delhi
        88, 87, 86, 85, 84, 87, 86, 85, 84, 83,        # GTBIT
        90, 89, 88, 87, 86, 89, 88, 87, 86, 85,        # JMI
        91, 90, 89, 88, 87, 90, 89, 88, 87, 86,        # USICT
        89, 88, 87, 86, 85, 88, 87, 86, 85, 84,        # ADGITM
        88, 87, 86, 85, 84, 87, 86, 85, 84, 83,        # BVCOE
        87, 86, 85, 84, 83, 86, 85, 84, 83, 82,        # HMRITM
        86, 85, 84, 83, 82, 85, 84, 83, 82, 81,        # NIEC
        89, 88, 87, 86, 85, 88, 87, 86, 85, 84,        # Maharaja Surajmal
        87, 86, 85, 84, 83, 86, 85, 84, 83, 82,        # BPIT
        92, 91, 90, 89, 88, 91, 90, 89, 88, 87,        # IPU Main Campus
        85, 84, 83, 82, 81, 84, 83, 82, 81, 80         # Ambedkar Institute
    ]
}

df = pd.DataFrame(college_data)


# Trend Data (2015–2025)

trend_data = {
    "Year": list(range(2015, 2025 + 1)),
    "Average_Cutoff": [60, 63, 65, 67, 70, 73, 75, 78, 80, 83, 85]
}

trend_df = pd.DataFrame(trend_data)


# Functions

def best_suited(percentile):
    return df[df["Cutoff_2025"] <= percentile]

def additional_options(percentile):
    suited = best_suited(percentile).index
    return df[(df["Cutoff_2025"] <= percentile + 5) & ~(df.index.isin(suited))]

def show_all_cutoffs():
    return df
    
def get_trend_data():
    data = {
        "Year": list(range(2015, 2026)),
        "Cutoff_Percentile": [82.5, 84.2, 85.1, 86.8, 88.0, 89.5, 90.2, 91.0, 92.3, 93.8, 94.6]
    }
    return pd.DataFrame(data)

def plot_trend_bar_graph():
    years = trend_df["Year"]
    values = trend_df["Average_Cutoff"]

    plt.figure(figsize=(10, 5))
    plt.bar(years, values)
    plt.ylim(60, 100)
    plt.xlabel("Year")
    plt.ylabel("Average Percentile")
    plt.title("Cutoff Trend (2015–2025)")
    plt.tight_layout()
    plt.show()

