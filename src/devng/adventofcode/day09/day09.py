#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

import re
import itertools

line_regex = re.compile(r"(\w+) to (\w+) = (\d+)")

cities = set()
distances = dict()


def parse_line(line):
    m = line_regex.match(line)
    if m:
        city1 = m.group(1)
        city2 = m.group(2)
        distance = int(m.group(3))
        cities.add(city1)
        cities.add(city2)
        distances[(city1, city2)] = distance
    else:
        raise ValueError("Invalid line: " + line)


def find_route():
    shortest = None
    longest = None
    for route in itertools.permutations(cities):
        cur_lenght = 0
        for i in range(len(route) - 1):
            city1 = route[i]
            city2 = route[i + 1]
            if (city1, city2) in distances:
                cur_lenght += distances[(city1, city2)]
            elif (city2, city1) in distances:
                cur_lenght += distances[(city2, city1)]
            else:
                print("Not path from", city1, "to", city2)

        if not shortest or cur_lenght < shortest:
            shortest = cur_lenght
        if not longest or cur_lenght > longest:
            longest = cur_lenght
    return shortest, longest


def process_file(filename):
    with open(filename, "r") as f:
        for line in f:
            parse_line(line)
        return find_route()


def main():
    r = process_file("input.txt")
    print("Shortest route: %d\nLongest route:  %d" % r)


if __name__ == "__main__":
    main()
