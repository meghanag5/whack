import pandas as pd
path = 'crime_24.csv'
crime_data = pd.read_csv(path)
# crime_data.info()
# crime_data.head()

crime_data = crime_data.replace('-', pd.NA)

# Define columns to convert to numeric (skip the first column which is 'County')
numeric_columns = crime_data.columns[1:]

# Remove commas and percentage signs, then convert to numeric
crime_data[numeric_columns] = crime_data[numeric_columns].replace({',': '', '%': ''}, regex=True)
crime_data[numeric_columns] = crime_data[numeric_columns].apply(pd.to_numeric, errors='coerce')
#displays counties
unique_counties = crime_data['County'].unique()

print(unique_counties[:]) 

# crime_data.info()
# crime_data.head()





