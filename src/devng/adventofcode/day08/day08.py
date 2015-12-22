#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

import re


def process_file(filename):
    result = 0
    result2 = 0
    with open(filename, "r") as fin:
        for line in fin:
            s = line.strip()
            r = eval(line) # evaluated, needed for part 1
            e = re.escape(s) # encoded, needed for part 2
            result += len(s) - len(r)
            result2 += len(e) - len(s) + 2 # add 2 for the surrounding quotes of the new string
    return result, result2


def main():
    r = process_file("input.txt")
    print("Answer part one: %d.\nAnswer part two: %d" % r)


if __name__ == "__main__":
    main()
