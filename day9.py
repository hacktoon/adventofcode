#  Advent of code
#  Day 9: All in a Single Night

'''
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?
'''

from itertools import permutations


def parse(dt):
    ''' parse an expression like 'London to Belfast = 518 '''
    l = dt.strip().split(' ')
    return (l[0], l[2], int(l[4]))

with open('day9.txt') as f:
    raw_distances = f.readlines()

cities = set()
distances = {}
routes = []

for dt in raw_distances:
    dist_info = parse(dt)
    from_city = dist_info[0]
    to_city = dist_info[1]
    cities = cities.union({from_city, to_city})
    distances[(from_city, to_city)] = distances[(to_city, from_city)] = dist_info[2]

for route in permutations(cities):
    total_distance = 0
    for idx, city in enumerate(route[:-1]):
        route_key = (city, route[idx+1])
        total_distance += distances[route_key]
    else:
        routes.append({'route': route, 'distance': total_distance})

routes = sorted(routes, key=lambda x: x['distance'])
print('Shortest route is {!r}, with distance = {!r}'.format(routes[0]['route'], routes[0]['distance']))


'''
--- Part Two ---
The next year, just to show off, Santa decides to take the route with the longest distance instead.
He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.
For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.
What is the distance of the longest route?

'''

print('Longest route is {!r}, with distance = {!r}'.format(routes[-1]['route'], routes[-1]['distance']))
