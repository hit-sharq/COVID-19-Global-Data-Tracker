import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df_filtered = pd.read_csv('owid-covid-data.csv')
df_filtered = df_filtered[df_filtered['location'].isin(['Kenya', 'USA', 'India'])]
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Plot cumulative vaccinations over time for selected countries
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='total_vaccinations', hue='location')
plt.title('Cumulative COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend(title='Country')
plt.savefig('cumulative_vaccinations_over_time.png')
plt.close()

# Compare % vaccinated population
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='people_vaccinated_per_hundred', hue='location')
plt.title('Percentage of Population Vaccinated Over Time')
plt.xlabel('Date')
plt.ylabel('People Vaccinated per Hundred')
plt.legend(title='Country')
plt.savefig('percentage_population_vaccinated.png')
plt.close()
