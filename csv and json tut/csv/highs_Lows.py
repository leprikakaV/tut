import csv
from matplotlib import pyplot as plt
from datetime import  datetime

filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs, dates, lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, "нету данных")
        else:
            highs.append(high)
            dates.append(date)
            lows.append(low)


for index, column_header in enumerate(header_row):
    print(index, column_header)

fig = plt.figure(dpi=81, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)
plt.title("tutorial", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("температура в F", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()