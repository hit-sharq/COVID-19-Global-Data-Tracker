import pandas as pd

# Load the dataset
df = pd.read_csv('owid-covid-data.csv')

# Filter countries of interest
countries = ['Kenya', 'USA', 'India']
df_filtered = df[df['location'].isin(countries)]

# Drop rows with missing dates or critical values
df_filtered = df_filtered.dropna(subset=['date', 'total_cases', 'total_deaths'])

# Convert date column to datetime
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Handle missing numeric values with fillna or interpolate
df_filtered['total_cases'] = df_filtered['total_cases'].fillna(method='ffill')
df_filtered['total_deaths'] = df_filtered['total_deaths'].fillna(method='ffill')

# Preview cleaned data
print(df_filtered.head())
