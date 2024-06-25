total_cost = 0.0

with open('D:\Education\Python Mastery\python-mastery\Data\portfolio.dat', 'r') as f:
    for line in f:
        columns = line.split()
        total_cost += int(columns[1]) * float(columns[2])

print(total_cost)
