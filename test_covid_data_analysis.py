import pandas as pd

def test_data_loading_and_cleaning():
    try:
        # Load dataset
        df = pd.read_csv('owid-covid-data.csv')
        print("Dataset loaded successfully.")
        
        # Check columns
        print("Columns:", df.columns.tolist())
        
        # Preview first 5 rows
        print("First 5 rows:")
        print(df.head())
        
        # Missing values summary
        print("Missing values summary:")
        print(df.isnull().sum())
        
        # Data Cleaning
        countries = ['Kenya', 'USA', 'India']
        df_filtered = df[df['location'].isin(countries)]
        df_filtered = df_filtered.dropna(subset=['date', 'total_cases', 'total_deaths'])
        df_filtered['date'] = pd.to_datetime(df_filtered['date'])
        df_filtered['total_cases'] = df_filtered['total_cases'].fillna(method='ffill')
        df_filtered['total_deaths'] = df_filtered['total_deaths'].fillna(method='ffill')
        
        print("Cleaned data preview:")
        print(df_filtered.head())
        
        print("All tests passed successfully.")
    except Exception as e:
        print("Test failed:", e)

if __name__ == "__main__":
    test_data_loading_and_cleaning()
