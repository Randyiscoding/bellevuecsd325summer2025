import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
    f.close()

while True:
    while True:
        # Use Instructions
        hilow = input("Welcome to the Sitka Weather App!\n To View temperature Highs: Type 'H'\n To view temperature Lows: "
                  "Type 'L'\n To Quit: Type 'Q'")
        if hilow.upper() == 'L' or hilow.upper() == 'H' or hilow.upper() == 'Q':
            break
        else:
            print("Incorrect input. Try Again")

    if hilow.upper() == 'Q':
        print("Thank you for using the Sitka Weather App. Have a Sunny Day. Goodbye!")
        break
        sys.exit(1)
    elif hilow.upper() == 'H':
        # Plot the High temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily high temperatures - 2018", fontsize=24)
    else:
        # Plot the low temperatures.
        #plt.style.use('seaborn')
        figs, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low temperatures - 2018", fontsize=24)

    # Format plot.
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()