path = "csvs.csv"
from datetime import datetime
import csv

file = open(path, newline = '')

reader = csv.reader(file)

header = next(reader)

print(header)

data = []

for d in reader:
    dates = datetime.strptime(d[0], '%m/%d/%Y')
    open_price = float(d[1])
    high = float(d[2])
    low = float(d[3])
    close = float(d[4])
    volume = int(d[5])
    adjoint_close = float(d[6])

    data.append([dates, open_price, high, low, close, volume, adjoint_close])

print(data)