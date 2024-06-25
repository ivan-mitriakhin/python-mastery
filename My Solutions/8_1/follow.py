import os
import time

def follow(filename):
    with open(filename) as f:
        f.seek(0, os.SEEK_END)

        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)
                continue
            yield line

if __name__ == '__main__':
    for line in follow('Data/stocklog.csv'):
        row = line.split(',')
        name = row[0].strip('"')
        price = float(row[1])
        change = float(row[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))