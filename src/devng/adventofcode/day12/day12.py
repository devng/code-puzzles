#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

import json
import itertools

exclude_val = None

def process_json(s):
    j = json.loads(s)
    return traverse(j)

def traverse(obj):
    if isinstance(obj, dict):
        if exclude_val and exclude_val in obj.values():
            return 0
        else:
            return sum([traverse(v) for k, v in obj.items()])
    elif isinstance(obj, list):
        return sum([traverse(elem) for elem in obj])
    elif isinstance(obj, int):
        return obj
    else:
        return 0


def main():
    global exclude_val
    with open("input.txt", "r") as fin:
        for line in fin:
            r1 = process_json(line)
            exclude_val = "red"
            r2 = process_json(line)
            print("Answer part one: %d\nAnswer part two: %d" % (r1, r2))


if __name__ == "__main__":
    main()
