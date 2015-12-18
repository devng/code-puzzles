#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

import math
import itertools

# http://mathworld.wolfram.com/ConwaysConstant.html
CONWAY_CONST = 1.303577269034296


def look_and_say(s):
    last_d = None
    count = 0
    result = []
    for d in s:
        if last_d and d != last_d:
            result.append(str(count))
            result.append(last_d)
            count = 0
            last_d = d
        last_d = d
        count += 1
    result.append(str(count))
    result.append(last_d)
    return "".join(result)


def look_and_say_2(s):
    """
    Taken from: https://www.reddit.com/r/adventofcode/comments/3w8lmu/day_10_the_power_of_pythons_itertools/?
    """
    new_s = []
    for c, l in itertools.groupby(s):
        new_s.append(str(len(list(l))))
        new_s.append(c)
    return "".join(new_s)


def look_and_say_len(start_l, iterations=10):
    """
    This function is using Conway's Constant to compute an aproximation of the length
    of the look and say sequence.
    """
    for _ in range(iterations):
        start_l = math.ceil(start_l * CONWAY_CONST)
    return start_l


def main():
    s = "1113222113"

    for i in range(40):
        s = look_and_say(s)

    print(len(s))


if __name__ == "__main__":
    main()
    # print(look_and_say_len(1, 40))
