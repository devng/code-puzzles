#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

import hashlib
import sys


def check_num(key, num, prefix="00000"):
    input = key + str(num)
    h = hashlib.md5(input.encode('utf-8')).hexdigest()
    # print(key, num, h) # DEBUG
    return h.startswith(prefix)


def check_range(key, start=0, limit=1000, prefix="00000"):
    for i in range(start, start + limit):
        if check_num(key, i, prefix):
            return i
    return None


def main():
    key = "iwrupvqb"
    if len(sys.argv) != 3:
        print("Usage: ./day04.py <start> <limit>")
        exit(1)

    start = int(sys.argv[1])
    limit = int(sys.argv[2])
    n = check_range(key, start, limit) # Part 1
    # n = check_range(key, start, limit, "000000") # part 2

    if n:
        print("The answer is:", n)
    else:
        print("Could not find an answer.")


if __name__ == "__main__":
    main()
