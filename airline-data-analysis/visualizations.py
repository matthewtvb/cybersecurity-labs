# visualizations.py
# Creates a bar chart of airline delay rates from SQL query results

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Matth\python\sql_by_airline.csv")

# Shorten long airline names
name_map = {
    "GoJet Airlines LLC d/b/a United Express": "GoJet",
    "JetBlue Airways": "JetBlue",
    "PSA Airlines Inc.": "PSA Airlines",
    "Endeavor Air Inc.": "Endeavor Air",
    "Spirit Airlines": "Spirit",
    "Allegiant Air": "Allegiant",
    "Frontier Airlines": "Frontier",
    "Republic Airline": "Republic",
    "Hawaiian Airlines Network": "Hawaiian",
    "Alaska Airlines Network": "Alaska",
    "SkyWest Airlines Inc.": "SkyWest",
    "American Airlines Network": "American",
    "Delta Air Lines Network": "Delta",
    "Southwest Airlines": "Southwest",
    "Envoy Air": "Envoy",
    "Horizon Air": "Horizon",
    "United Air Lines Network": "United",
    "CommuteAir LLC dba CommuteAir": "CommuteAir",
    "Piedmont Airlines": "Piedmont",
    "Mesa Airlines Inc.": "Mesa",
}
df["carrier_name"] = df["carrier_name"].map(name_map).fillna(df["carrier_name"])

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df["carrier_name"], df["delay_rate_pct"], color="steelblue")
ax.invert_yaxis()
ax.set_xlabel("Delay Rate (%)")
ax.set_title("U.S. Airline Delay Rate — December 2025", fontweight="bold")

plt.tight_layout()
plt.savefig(r"C:\Users\Matth\python\chart_delay_by_airline.png", dpi=150)
plt.close()
print("Saved: chart_delay_by_airline.png")
