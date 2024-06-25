from structure import Structure
import sys

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares -= nshares

if __name__ == '__main__':
    s = Stock(name='GOOG',shares=100,price=490.1)
    print(s.name)