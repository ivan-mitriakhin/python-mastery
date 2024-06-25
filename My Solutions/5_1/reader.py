import csv
import tracemalloc
from sys import intern
import collections.abc
from abc import ABC, abstractmethod
from typing import List, TextIO, TypeVar, Type
from stock import Stock

T = TypeVar('T')

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return {name:func(val) for name, func, val in zip(headers, self.types, row)}
    
class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)

def csv_as_instances(lines: TextIO, cls: Type[T], headers: List[str] = None) -> List[Type[T]]:
    '''
    Convert lines of CSV data into a list of instances
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records


def csv_as_dicts(lines: TextIO, types: List[str], headers: List[str] = None) -> List[dict]:
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = { name: func(val)
                   for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def read_csv_as_instances(filename: str, cls: Type[T], headers: List[str] = None) -> List[Type[T]]:
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as f:
        return csv_as_instances(f, cls, headers)
    
def read_csv_as_dicts(filename: str, types: List[str], headers: List[str] = None) -> List[dict]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as f:
        return csv_as_instances(f, types, headers)   

if __name__ == "__main__":
    import stock
    port = read_csv_as_instances('Data/portfolio.csv', stock.Stock)
    print(port)