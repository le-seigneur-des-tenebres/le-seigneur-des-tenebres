"""
import csv

from datetime import datetime
from matplotlib import pyplot as plt

# Get dates and highs from file.
filename_1 = 'death_valley_2014.csv'
filename_2 = 'sitka_weather_07-2014.csv'

with open(filename_1) as f1:
    reader_1 = csv.reader(f1)
    header_1 = next(reader_1)
    #print(header_1)

    dates_1, highs_1, lows_1 = [],[], []
    for row in reader_1:
        current_date_1 = datetime.strptime(row[0], "%Y-%m-%d")
        dates_1.append(current_date_1)

        high_1 = int(row[1])
        highs_1.append(high_1)

        low_1 = int(row[3])
        lows_1.append(low_1)

with open(filename_2) as f2:
    reader_2 = csv.reader(f2)
    header_2 = next(reader_2)
    #print(header_2)

    dates_2, highs_2, lows_2 = [], [], []
    for row in reader_2:
        current_date_2 = datetime.strptime(row[0], "%Y-%m-%d")
        dates_2.append(current_date_2)

        high_2 = int(row[1])
        highs_2.append(high_2)

        low_2 = int(row[3])
        lows_2.append(low_2)

#Plot data.

fig = plt.figure(dpi=128, figusize=(10,6))
plt.plot(dates_1, highs_1, c='red')
plt.plot(dates_2, highs_2, c='blue')

#Format plot.
plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

"""
"""
import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

"""

import csv

#Get temperature from file.
filename = 'death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []

    for row in reader:
        highs.append(row[4])
    print(highs)