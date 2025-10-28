import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# College data
college_data = {
    'College': ['DTU', 'NSIT', 'IIIT Delhi', 'IGDTUW', 'MAIT', 'BVP', 'MSIT', 'JMI'],
    'Branch': ['CSE', 'ECE', 'IT', 'CSE', 'ECE', 'EE', 'IT', 'CSE'],
    'Min_Percentile': [98, 96, 94, 92, 90, 88, 87, 85],
    'Max_Percentile': [100, 99, 97, 95, 94, 92, 90, 88]
}

df = pd.DataFrame(college_data)

# Trend data
trend_data = {
    'Year': list(range(2015, 2026)),  # till 2025
    'DTU': [96, 97, 97, 98, 98, 99, 98, 98, 98, 98, 98],
    'NSIT': [95, 96, 96, 97, 97, 98, 97, 97, 97, 97, 97],
    'IIIT Delhi': [93, 93, 94, 94, 95, 95, 96, 96, 96, 97, 97],
    'IGDTUW': [90, 91, 91, 92, 92, 93, 93, 94, 94, 95, 95]
}
trend_df = pd.DataFrame(trend_data)

# Predict next 2 years (2026 & 2027)
def predict_future_cutoffs():
    model = LinearRegression()
    X = trend_df[['Year']]
    future_years = [2026, 2027]

    future_preds = {'Year': future_years}
    for college in ['DTU', 'NSIT', 'IIIT Delhi', 'IGDTUW']:
        y = trend_df[college]
        model.fit(X, y)
        preds = model.predict(np.array(future_years).reshape(-1, 1))
        future_preds[college] = preds

    return pd.DataFrame(future_preds)

def get_full_trend_data():
    """Return past + predicted trend data"""
    future_df = predict_future_cutoffs()
    full_df = pd.concat([trend_df, future_df], ignore_index=True)
    full_df = full_df.round(2)
    return full_df

def best_suited(user_percentile):
    return df[(df['Min_Percentile'] <= user_percentile) & (df['Max_Percentile'] >= user_percentile)]

def backup_options(user_percentile):
    return df[df['Min_Percentile'] < user_percentile - 3]

def show_all():
    return df
