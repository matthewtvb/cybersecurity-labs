# Matthew Tran 
# airline_delay_analysis.py
# Analyzes U.S. airline on-time performance data from the Bureau of Transportation Statistics (BTS)
# Dataset: https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp
# Download the CSV and place it in the same folder as this script, named: airline_delay_data.csv

import pandas as pd

# STEP 1: LOAD THE DATA
# Read the CSV file into a DataFrame (think of it like loading a spreadsheet into Python)
df = pd.read_csv("airline_delay_data.csv")

# Show the first 5 rows so we can see what the data looks like
print("=== Preview of raw data ===")
print(df.head())
print(f"\nTotal rows loaded: {len(df)}")
print(f"Columns: {list(df.columns)}\n")

# STEP 2: CLEAN THE DATA
# Strip whitespace from column names (CSVs often have hidden spaces)
df.columns = df.columns.str.strip()

# Drop any rows where key columns are missing
df = df.dropna(subset=["carrier_name", "arr_del15", "arr_flights"])

# Convert delay columns to numbers (they sometimes load as text)
df["arr_del15"] = pd.to_numeric(df["arr_del15"], errors="coerce")
df["arr_flights"] = pd.to_numeric(df["arr_flights"], errors="coerce")
df["carrier_delay"] = pd.to_numeric(df["carrier_delay"], errors="coerce")
df["weather_delay"] = pd.to_numeric(df["weather_delay"], errors="coerce")
df["nas_delay"] = pd.to_numeric(df["nas_delay"], errors="coerce")

# Drop any rows that had bad values after conversion
df = df.dropna(subset=["arr_del15", "arr_flights"])

print(f"Rows after cleaning: {len(df)}\n")

# STEP 3: ANALYSIS — Question 1
# Which airlines have the highest delay rate?
# Group the data by airline, then sum up total flights and delayed flights
airline_summary = df.groupby("carrier_name").agg(
    total_flights=("arr_flights", "sum"),
    delayed_flights=("arr_del15", "sum")
).reset_index()

# Calculate the delay rate as a percentage
airline_summary["delay_rate_%"] = (
    airline_summary["delayed_flights"] / airline_summary["total_flights"] * 100
).round(2)

# Sort from highest to lowest delay rate
airline_summary = airline_summary.sort_values("delay_rate_%", ascending=False)

print("=== Question 1: Which airlines have the highest delay rate? ===")
print(airline_summary[["carrier_name", "total_flights", "delayed_flights", "delay_rate_%"]].to_string(index=False))
print()

# STEP 4: ANALYSIS — Question 2
# What are the most common causes of delays?
# Sum up each delay cause across all airlines and flights
delay_causes = {
    "Carrier (Airline)": df["carrier_delay"].sum(),
    "Weather":           df["weather_delay"].sum(),
    "National Air System": df["nas_delay"].sum(),
}

# Calculate total delay minutes to find each cause's share
total_delay_minutes = sum(delay_causes.values())

print("=== Question 2: What causes the most delays? ===")
for cause, minutes in sorted(delay_causes.items(), key=lambda x: x[1], reverse=True):
    pct = (minutes / total_delay_minutes * 100) if total_delay_minutes > 0 else 0
    print(f"  {cause}: {int(minutes):,} minutes ({pct:.1f}%)")
print()

# STEP 5: ANALYSIS — Question 3
# Which months have the most delays?
# Group by month and calculate delay rate per month
monthly = df.groupby("month").agg(
    total_flights=("arr_flights", "sum"),
    delayed_flights=("arr_del15", "sum")
).reset_index()

monthly["delay_rate_%"] = (
    monthly["delayed_flights"] / monthly["total_flights"] * 100
).round(2)

# Map month numbers to names so it's readable
month_names = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}
monthly["month_name"] = monthly["month"].map(month_names)
monthly = monthly.sort_values("delay_rate_%", ascending=False)

print("=== Question 3: Which months have the worst delays? ===")
print(monthly[["month_name", "total_flights", "delayed_flights", "delay_rate_%"]].to_string(index=False))
print()

# STEP 6: EXPORT RESULTS
# Save the airline summary to a CSV so it can be opened in Excel or Tableau
airline_summary.to_csv("airline_delay_summary.csv", index=False)
monthly.to_csv("monthly_delay_summary.csv", index=False)

print("=== Results saved to airline_delay_summary.csv and monthly_delay_summary.csv ===")
