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
    import csv
    lines = follow('Data/stocklog.csv')
    rows = csv.reader(lines)
    for row in rows:
        print(row)