#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

import itertools

eggnog = 150

def parse_file(filename):
    containers = []
    with open(filename, "r") as f:
        for line in f:
            containers.append(int(line))
    return containers


def find_solution_part1(containers):
    result = 0
    for i in range(len(containers)):
        for c in itertools.combinations(containers, i):
            if sum(c) == eggnog:
                result += 1
    return result


def find_solution_part2(containers):
    result = 0
    for i in range(len(containers)):
        for c in itertools.combinations(containers, i):
            if sum(c) == eggnog:
                result += 1
        if result > 0:
            break
    return result


def main():
    containers = parse_file("input.txt")

    r1 = find_solution_part1(containers)
    print("Answer part one: %d" % r1)

    r2 = find_solution_part2(containers)
    print("Answer part two: %d" % r2)


if __name__ == "__main__":
    main()
