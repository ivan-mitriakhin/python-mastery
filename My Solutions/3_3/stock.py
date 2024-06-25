import csv
from decimal import Decimal

class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    @classmethod
    def from_row(cls, row):
        values = [t(val) for t, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares -= nshares

class DStock(Stock):
    types = (str, int, Decimal)


def print_portfolio(portfolio):
    for s in portfolio:
        print(f'{s.name:10s} {s.shares:10d} {s.price:10.2f}')


if __name__ == "__main__":
    row = ['AA', '100', '32.20']
    s = DStock.from_row(row)
    print(type(s.price))
        