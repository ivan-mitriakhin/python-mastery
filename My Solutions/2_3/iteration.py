import csv
import sys
sys.path += ['My Solutions/2_2', 'My Solutions/2_1']

# f = open('Data/portfolio.csv')
# f_csv = csv.reader(f)
# headers = next(f_csv)
# rows = list(f_csv)

# for name, shares, price in rows:
#     print(name, shares, price)

# for name, *data in rows:
#     print(name, data)

# for id, (name, shares, price) in enumerate(rows):
#     print(id, name, shares, price)

# for row in rows:
#     print(dict(zip(headers, row)))

for n in (x*x for x in [1, 2, 3, 4, 5]):
    print(n)

print('#'*25)
# Generator expressions and reduction funcs

from readport import read_portfolio
portfolio = read_portfolio('Data/portfolio.csv')
s = portfolio[0].values()

print(sum(s['shares']*s['price'] for s in portfolio))
print(', '.join(str(x) for x in s))

print('#'*25)

import tracemalloc
tracemalloc.start()

import readrides
rows = readrides.read_rides_as_dicts('Data/ctabus.csv')
rt22 = [row for row in rows if row['route'] == '22']

print(max(rt22, key=lambda row: row['rides']))
print('Average current memory [MB], average peak memory [MB]:', [mem / (1024*1024) for mem in tracemalloc.get_traced_memory()])
tracemalloc.stop()

print('#'*25)
# Saving a lot of memory

tracemalloc.start()
f = open('Data/ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)
rows = (dict(zip(headers, row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')

print(max(rt22, key=lambda row: int(row['rides'])))
print('Average current memory [MB], average peak memory [MB]:', [mem / (1024*1024) for mem in tracemalloc.get_traced_memory()])
tracemalloc.stop()