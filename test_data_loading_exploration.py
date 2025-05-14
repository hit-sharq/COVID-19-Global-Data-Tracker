import pandas as pd

# Load the dataset
df = pd.read_csv('owid-covid-data.csv')

# Check columns
print(df.columns)

# Preview first 5 rows
print(df.head())

# Identify missing values
print(df.isnull().sum())
