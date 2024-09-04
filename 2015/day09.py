import itertools
from collections import defaultdict

from input_reader import puzzle_input


def part1():
    distances = defaultdict(list)
    cities = set()
    list_distances = []
    for i in puzzle_input():
        a, _, b, _, c = i.split(' ')
        distances[int(c.strip('\n'))].append({a, b})
        cities.add(a)
        cities.add(b)
    print(distances)
    print(list(distances.values()))
    ways = list(itertools.permutations(cities))
    for way in ways:
        travel_distance = 0
        for i in range(1, len(cities)):
            travel_distance += list(distances.keys())[[num for num, j in enumerate(list(distances.values())) if {way[i - 1], way[i]} in j][0]]
        list_distances.append(travel_distance)
    print(min(list_distances))
    print(max(list_distances))


part1()
