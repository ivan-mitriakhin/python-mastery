import csv
from decimal import Decimal

class Stock:
    __slots__ = ('name', '_shares', '_price')
    _types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'Expected {self._types[1]}')
        if value < 0:
            raise ValueError('shares must be >= 0')
        self._shares = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f'Expected {self._types[2]}')
        if value < 0:
            raise ValueError('price must be >= 0')
        self._price = value

    @property
    def cost(self):
        return self.shares * self.price

    @classmethod
    def from_row(cls, row):
        values = [t(val) for t, val in zip(cls._types, row)]
        return cls(*values)
    
    def sell(self, nshares):
        self.shares -= nshares

class DStock(Stock):
    _types = (str, int, Decimal)


def print_portfolio(portfolio):
    for s in portfolio:
        print(f'{s.name:10s} {s.shares:10d} {s.price:10.2f}')


if __name__ == "__main__":
    row = ['AA', '100', '32.20']
    s = DStock.from_row(row)
    print(s.price)
        