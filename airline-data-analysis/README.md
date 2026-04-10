# U.S. Airline Delay Analysis

## Overview
Analyzes U.S. airline on-time performance data from the Bureau of Transportation Statistics (BTS)
to identify delay trends by airline, cause, and month.

## Dataset
Source: https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp  
Download the CSV and place it in the same folder as the script, named: airline_delay_data.csv

## What the script does
1. Loads and cleans 1,800+ records of flight delay data
2. Calculates delay rates by airline
3. Breaks down delay causes (carrier, weather, national air system)
4. Identifies which months have the worst delays
5. Exports results to CSV for further analysis in Excel or Tableau

## Key Findings (December 2025)
1. GoJet Airlines had the highest delay rate at 40.6%
2. Airline-caused delays accounted for 56% of all delay minutes
3. Weather was responsible for only 11% of delays

## How to run
1. Install pandas: pip install pandas
2. Place airline_delay_data.csv in the same folder as the script
3. Run: python airline_delay_analysis.py

## Tools Used
Python, pandas
