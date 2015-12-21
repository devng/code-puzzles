#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

import re
import itertools

line_regex = re.compile(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)")

happiness_dict = dict()
guests = set()


def parse_file(filename):
    with open(filename, "r") as f:
        for line in f:
            m = line_regex.match(line)
            if m:
                guest1 = m.group(1)
                lose_gain = m.group(2)
                happiness = int(m.group(3))
                guest2 = m.group(4)
                guests.add(guest1)
                guests.add(guest2)
                if lose_gain == "lose":
                    happiness_dict[(guest1, guest2)] = -1 * happiness
                else:
                    happiness_dict[(guest1, guest2)] = happiness
            else:
                raise ValueError("Invalid line: " + line)


def compute_hapiness(seating_arrangement):
    happiness = 0
    size = len(seating_arrangement)
    for i in range(size):
        n1 = seating_arrangement[i - 1]
        g = seating_arrangement[i]
        n2 = seating_arrangement[(i + 1) % size]
        if (g, n1) in happiness_dict:
            happiness += happiness_dict[(g, n1)]
        if (g, n2) in happiness_dict:
            happiness += happiness_dict[(g, n2)]

    return happiness


def find_best_seating_arrangement(filename, add_myself=False):
    parse_file(filename)
    if add_myself:
        guests.add("Me")
    happiness = 0
    for seating_arrangement in itertools.permutations(guests):
        h = compute_hapiness(seating_arrangement)
        happiness = max(happiness, h)
    return happiness


if __name__ == "__main__":
    h1 = find_best_seating_arrangement("input.txt")
    h2 = find_best_seating_arrangement("input.txt", True)
    print("Answer part one: %s\nAnswer part two: %s" % (h1, h2))
