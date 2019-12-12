import os
import sqlite3
import pandas as pd


# Create pandas dataframe
df = pd.read_csv('buddymove_holidayiq.csv')

# Initiate SQL connection
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

# Insert the data into a new table
df.to_sql('review', conn, index=False)

# Count number of rows
curs.execute("SELECT COUNT ('User Id') \
              FROM review \
              ;")
print('Num rows:', curs.fetchall()[0][0])

# Nature AND Shopping
curs.execute("SELECT COUNT ('User Id') \
              FROM review \
              WHERE Nature >= 100 \
              AND Shopping >=100 \
              ;")
print("Nature & Shopping:", curs.fetchall()[0][0])
