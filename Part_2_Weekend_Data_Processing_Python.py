import pandas as pd
from datetime import datetime

# Load Saturday and Sunday CSV files
saturday_data = pd.read_csv('data_2023-02-11.csv')
sunday_data = pd.read_csv('data_2023-02-12.csv')

# Combine data from both files
combined_data = pd.concat([saturday_data, sunday_data], ignore_index=True)

# Add a new column for the generation date
generation_date = datetime.today().strftime('%Y-%m-%d')
combined_data['Generation_Date'] = generation_date

# Save the combined data to a new CSV file
combined_data.to_csv('data_2023-02-13.csv', index=False)

print("Combined data saved to 'data_2023-02-13'")
