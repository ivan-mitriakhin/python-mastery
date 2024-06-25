import csv
import tracemalloc
from sys import intern
import collections.abc

class DataCollection(collections.abc.Sequence):
    def __init__(self, headers, types):
        self.headers = headers
        self.types = types
        self.n_columns = len(self.headers)
        self.columns = [[] for _ in range(self.n_columns)]

    def __getitem__(self, index):
        return { self.headers[i]:self.types[i](self.columns[i][index]) for i in range(self.n_columns) }
    
    def __len__(self):
        return len(self.columns[0])
    
    def append(self, record):
        for i in range(self.n_columns):
            self.columns[i].append(record[i])

def read_csv_as_instances(filename, cls):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
        return records


def read_csv_as_dicts(filename, types):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {name:func(val) for name, func, val in zip(headers, types, row)}
            records.append(record)
    return records

def read_csv_as_columns(filename, types):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = DataCollection(headers, types)
        for row in rows:
            records.append(row)
    return records

if __name__ == "__main__":
    tracemalloc.start()
    rows = read_csv_as_columns('Data/ctabus.csv', [intern,str,str,int])
    routes = { row['route'] for row in rows }
    print(len(routes))
    routeids = { id(row['route']) for row in rows }
    print(len(routeids))
    print(tracemalloc.get_traced_memory())