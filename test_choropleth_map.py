import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('owid-covid-data.csv')

# Prepare dataframe with iso_code and total_cases for the latest date
latest_date = df['date'].max()
df_latest = df[df['date'] == latest_date]
df_latest = df_latest[['iso_code', 'location', 'total_cases', 'total_vaccinations']]

# Plot choropleth map showing case density
fig = px.choropleth(df_latest, locations='iso_code', color='total_cases', hover_name='location',
                    color_continuous_scale='Reds',
                    title='COVID-19 Total Cases by Country')
fig.write_html('choropleth_total_cases.html')

# Optional: Plot choropleth map showing vaccination rates
fig2 = px.choropleth(df_latest, locations='iso_code', color='total_vaccinations', hover_name='location',
                     color_continuous_scale='Blues',
                     title='COVID-19 Total Vaccinations by Country')
fig2.write_html('choropleth_total_vaccinations.html')
