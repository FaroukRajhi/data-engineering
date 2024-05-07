# Load CSV to SQLite with pandas

import pandas as pd
import sqlite3 as 

- Read the database CSV file

data = pd.read_csv('file.csv')

- Connect to the database
conn = sqlite3.connect('database.db')


data.to_sql('table',conn)

# Retrieve data from database using pandas

df = pd.read_sql("SELECT  * FROM table", conn)
print df