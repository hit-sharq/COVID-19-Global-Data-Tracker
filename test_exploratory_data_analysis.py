import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df_filtered = pd.read_csv('owid-covid-data.csv')
df_filtered = df_filtered[df_filtered['location'].isin(['Kenya', 'USA', 'India'])]
df_filtered = df_filtered.dropna(subset=['date', 'total_cases', 'total_deaths'])
df_filtered['date'] = pd.to_datetime(df_filtered['date'])
df_filtered['total_cases'] = df_filtered['total_cases'].fillna(method='ffill')
df_filtered['total_deaths'] = df_filtered['total_deaths'].fillna(method='ffill')

# Plot total cases over time for selected countries
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='total_cases', hue='location')
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend(title='Country')
plt.savefig('total_cases_over_time.png')
plt.close()

# Plot total deaths over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='total_deaths', hue='location')
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend(title='Country')
plt.savefig('total_deaths_over_time.png')
plt.close()

# Compare daily new cases between countries
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='new_cases', hue='location')
plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend(title='Country')
plt.savefig('daily_new_cases.png')
plt.close()

# Calculate death rate
df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases']
print(df_filtered[['location', 'date', 'death_rate']].head())
