import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

path = Path("weather_data/Kentucky Temperatures 2025.csv")
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for i, header in enumerate(header_row):
    print(i, header)
    
# Extracting dates, highs, lows for temperature
dates, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
fig, ax = plt.subplots()

ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='green', alpha=0.5)

ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.5)

ax.set_title("Kentucky Daily High and Low Temperatures, 2025", fontsize=20)
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Temperature (F)", fontsize=14)
fig.autofmt_xdate()
ax.tick_params(labelsize=14)

plt.show()