import pandas as pd
import sqlite3

# Load to csv
csv = 'sysarmy_survey_2020_processed.csv'
df = pd.read_csv(csv)
#print(df.head())

# Creating/Connect SQLite database
connection = sqlite3.connect('database.db')

# Insert the data from the DataFrame into the SQLite table
df.to_sql('new_db_sql',connection,if_exists='replace')

# Printing pandas dataframe
print('data frame')
pd.read_sql('''SELECT * FROM new_db_sql''', connection)






