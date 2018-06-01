#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

import re
from collections import defaultdict
import operator

line_regex = re.compile(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")


def parse_file(filename):
    result = {}
    with open(filename, "r") as f:
        for line in f:
            m = line_regex.match(line)
            if m:
                name = m.group(1)
                speed = int(m.group(2))
                t_speed = int(m.group(3))
                t_rest = int(m.group(4))
                result[name] = (speed, t_speed, t_rest)
            else:
                raise ValueError("Invalid line: "  + line)
    return result


def race_distance(duration, speed, t_speed, t_rest):
    t = t_speed + t_rest
    d = (duration // t) * speed * t_speed
    r = min(duration % t, t_speed)
    d += r * speed

    return d


def all_distances(duration, reindeer_dict):
    result = []
    for k, v in reindeer_dict.items():
        d = race_distance(duration, v[0], v[1], v[2])
        result.append((k, d))
    result.sort(key=lambda tup: tup[1])
    result.reverse()
    return result


def all_points(duration, reindeer_dict):
    points = defaultdict(int)
    for i in range(1, duration + 1):
        all_d = all_distances(i, reindeer_dict)
        last_d = all_d[0][1]
        for d in all_d:
            reindeer = d[0]
            distance = d[1]
            if last_d == distance:
                points[reindeer] += 1
            else:
                break

    return points


def main():
    duration = 2503
    reindeer_dict = parse_file("input.txt")

    # Part one
    r1 = all_distances(duration, reindeer_dict)[0]
    print("The winner is %s with a total distnace of %d km." % r1)

    # Part two
    r2 = all_points(duration, reindeer_dict)
    reindeer = max(r2.items(), key=operator.itemgetter(1))[0]
    print("The winner is %s with a total distnace of %d km." % (reindeer, r2[reindeer]))


if __name__ == "__main__":
    main()
