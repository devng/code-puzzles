#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals


def find_house(goal, presents=10, max_deliveries=None):
    # Each house gets at least ten times its house number, so we know house
    # (target/10) succeeds
    max_houses = int(goal / presents)
    houses = [0 for _ in range(max_houses)]

    # No point in checking more elves than houses
    for elf in range(1,max_houses):
        limit = max_houses
        if max_deliveries:
            limit = min(max_houses, elf * (max_deliveries + 1))
        for house in range(elf, limit, elf):
            houses[house] += elf * presents

    for i in range(max_houses):
        if houses[i] >= goal:
            return i
    return 0


def main():
    goal = 33100000
    r1 = find_house(goal)
    print("Answer part one: %d" % r1)

    r2 = find_house(goal, 11, 50)
    print("Answer part two: %d" % r2)


if __name__ == "__main__":
    main()
