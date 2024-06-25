def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'r') as f:
        for line in f:
            columns = line.split()
            try:
                total_cost += int(columns[1]) * float(columns[2])
            except ValueError as e:
                print(f'Couldn\'t parse: {repr(line)}')
                print(f'Reason: {e}')

    return total_cost

print(portfolio_cost('D:\Education\Python Mastery\python-mastery\Data\portfolio3.dat'))