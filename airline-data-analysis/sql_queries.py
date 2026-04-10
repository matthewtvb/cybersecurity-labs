# sql_queries.py
# Runs SQL queries against the airline delays database

import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect(r"C:\Users\Matth\python\airline_delays.db")

# QUERY 1: Total delayed flights by airline
print("=== Query 1: Total delayed flights by airline ===")
q1 = pd.read_sql_query("""
    SELECT carrier_name, 
           SUM(arr_flights) AS total_flights,
           SUM(arr_del15) AS total_delayed,
           ROUND(SUM(arr_del15) * 100.0 / SUM(arr_flights), 2) AS delay_rate_pct
    FROM flight_delays
    GROUP BY carrier_name
    ORDER BY delay_rate_pct DESC
""", conn)
print(q1.to_string(index=False))
print()

# QUERY 2: Delay minutes by cause
print("=== Query 2: Delay minutes by cause ===")
q2 = pd.read_sql_query("""
    SELECT 'Carrier' AS cause, SUM(carrier_delay) AS total_minutes FROM flight_delays
    UNION ALL
    SELECT 'Weather' AS cause, SUM(weather_delay) FROM flight_delays
    UNION ALL
    SELECT 'National Air System' AS cause, SUM(nas_delay) FROM flight_delays
    UNION ALL
    SELECT 'Security' AS cause, SUM(security_delay) FROM flight_delays
    UNION ALL
    SELECT 'Late Aircraft' AS cause, SUM(late_aircraft_delay) FROM flight_delays
    ORDER BY total_minutes DESC
""", conn)
print(q2.to_string(index=False))
print()

# QUERY 3: Average delay minutes per flight by airline
print("=== Query 3: Average delay minutes per flight by airline ===")
q3 = pd.read_sql_query("""
    SELECT carrier_name,
           ROUND(SUM(arr_delay) * 1.0 / SUM(arr_flights), 2) AS avg_delay_per_flight
    FROM flight_delays
    GROUP BY carrier_name
    ORDER BY avg_delay_per_flight DESC
""", conn)
print(q3.to_string(index=False))
print()

# QUERY 4: Top 10 airports with the most delayed flights
print("=== Query 4: Top 10 airports with the most delayed flights ===")
q4 = pd.read_sql_query("""
    SELECT airport_name,
           SUM(arr_flights) AS total_flights,
           SUM(arr_del15) AS total_delayed,
           ROUND(SUM(arr_del15) * 100.0 / SUM(arr_flights), 2) AS delay_rate_pct
    FROM flight_delays
    GROUP BY airport_name
    ORDER BY total_delayed DESC
    LIMIT 10
""", conn)
print(q4.to_string(index=False))
print()

# Export results to CSV
q1.to_csv(r"C:\Users\Matth\python\sql_by_airline.csv", index=False)
q2.to_csv(r"C:\Users\Matth\python\sql_by_cause.csv", index=False)
q3.to_csv(r"C:\Users\Matth\python\sql_avg_delay.csv", index=False)
q4.to_csv(r"C:\Users\Matth\python\sql_top_airports.csv", index=False)

print("=== Done! Results saved to CSV files ===")

conn.close()
