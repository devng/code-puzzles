#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

from collections import defaultdict


def move(x, y, d):
    """
    :param x: the current coordinates on the x axis
    :param y: the current coordinates on the y axis
    :param d: a direction string must be one char from ^>v<
    :return: the new x,y coordinates
    """
    if d == '^':
        y += 1
    elif d == '>':
        x += 1
    elif d == 'v':
        y -= 1
    elif d == '<':
        x -= 1
    else:
        print("Unknown direction: " + d)

    return x, y


def count_houses(input, x=0, y=0):
    houses = defaultdict(int)
    houses[(x,y)] += 1
    for d in input:
        x, y = move(x, y, d)
        houses[(x, y)] += 1
    return len(houses.keys())


def count_houses_2(input, x=0, y=0):
    houses = defaultdict(int)
    x1 = x # Santa x
    x2 = x # Santa y
    y1 = y # Robo-Santa x
    y2 = y # Robo-Santa y
    houses[(x1, y1)] += 1
    houses[(x2, y2)] += 1
    for i in range(0, len(input), 2):
        x1, y1 = move(x1, y1, input[i])
        x2, y2 = move(x2, y2, input[i+1])
        houses[(x1, y1)] += 1
        houses[(x2, y2)] += 1
    return len(houses.keys())


def main():
    with open("input.txt", 'r') as fin:
        for line in fin:
            print("Answer part one: ", count_houses(line))
            print("Answer part two: ", count_houses_2(line))


if __name__ == "__main__":
    main()
