#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

# Taken from input.txt
# (name, capacity, durability, flavor, texture, calories)
ingredients = (
    ("Frosting", 4, -2, 0, 0, 5),
    ("Candy", 0, 5, -1, 0, 8),
    ("Butterscotch", -1, 0, 5, 0, 6),
    ("Sugar", 0, 0, -2, 2, 1)
)


def gen_distribution(size):
    n = size + 1
    for a in range(n):
        for b in range(n - a):
            for c in range(n - a - b):
                for d in range(n - a - b - c):
                    if a + b + c + d == size:
                        yield a, b, c, d


def compute_score(dist):
    r = [0] * 4
    cal = 0
    for i in range(len(dist)):
        for j in range(4):
            r[j] += ingredients[i][1 + j] * dist[i]
        cal += ingredients[i][5] * dist[i]
    result = 1
    for v in r:
        result *= max(v, 0)
    return result, cal


def solution_part1():
    score = 0
    for d in gen_distribution(100):
        score = max(compute_score(d)[0], score)
    print("Answer part one: %d" % score)


def solution_part2():
    score = 0
    for d in gen_distribution(100):
        s = compute_score(d)
        if s[1] == 500:
            score = max(s[0], score)
    print("Answer part two: %d" % score)


if __name__ == "__main__":
    solution_part1()
    solution_part2()
