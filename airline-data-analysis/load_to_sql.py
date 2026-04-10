# load_to_sql.py
# Loads the airline delay CSV into a SQLite database

import pandas as pd
import sqlite3

# Load the CSV
df = pd.read_csv(r"C:\Users\Matth\python\airline_delay_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Connect to a SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect(r"C:\Users\Matth\python\airline_delays.db")

# Load the dataframe into a SQL table called "flight_delays"
df.to_sql("flight_delays", conn, if_exists="replace", index=False)

print("Done! Database created at C:\\Users\\Matth\\python\\airline_delays.db")
print(f"Rows loaded: {len(df)}")

conn.close()
