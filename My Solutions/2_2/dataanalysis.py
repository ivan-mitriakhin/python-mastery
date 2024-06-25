import sys
sys.path.append('My Solutions/2_1')

import readrides
rows = readrides.read_rides_as_dicts('Data/ctabus.csv')

from collections import Counter, defaultdict

''' 
1st Question
'''
print('Q: How many bus routes exist in Chicago?')
uniq_routes = { d['route'] for d in rows }
print(f'A: {len(uniq_routes)}\n')

''' 
2nd Question
'''
print('Q: How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?')
by_row_date = dict()
for row in rows:
    by_row_date[row['route'], row['date']] = row['rides']

answer = by_row_date['22', '02/02/2011']
print(f'A: {answer}\n')

# # Uncomment if you want to pick a route and date yourself
# uniq_dates = { d['date'] for d in rows }
# while True:
#     route = input('Enter the bus route: ')
#     date = input('Enter the date in format DD/MM/YYYY: ')

#     if (route not in uniq_routes) or (date not in uniq_dates):
#         print('Wrong date or bus route, try again.')
#         continue

#     try:
#         by_row_date[route, date] = [d['rides'] for d in rows if d['route'] == route and d['date'] == date][0]
#     except IndexError:
#         print('No such bus route on that date.')

#     print(f'A: {by_row_date[route, date]}')
#     if input('Do you want to proceed (y/n)? ') == 'n':
#         break
# print()

'''
3rd Question
'''
print('Q: What is the total number of rides taken on each bus route?')
count_route_rides = dict()
for route in uniq_routes:       
    count_route_rides[route] = sum(d['rides'] for d in rows if d['route'] == route)
print(f'A: {count_route_rides}\n')

'''
4th Question
'''
print('Q: What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?')
rides_by_year = defaultdict(Counter)
for row in rows:
    year = row['date'].split('/')[2]
    rides_by_year[year][row['route']] += row['rides']

diffs = rides_by_year['2011'] - rides_by_year['2001']
print('A: ')
for route, diff in diffs.most_common(5):
    print(route, diff)