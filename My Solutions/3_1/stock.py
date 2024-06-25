import csv

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares -= nshares

def read_portfolio(filename):
    portfolio = []
    with open(filename, "r") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio.append(Stock(row[0], int(row[1]), float(row[2])))
    return portfolio

def print_portfolio(portfolio):
    for s in portfolio:
        print(f'{s.name:10s} {s.shares:10d} {s.price:10.2f}')


if __name__ == "__main__":
    portfolio = read_portfolio('Data/portfolio.csv')
    print_portfolio(portfolio)
        