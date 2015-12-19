#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

import json
import itertools


result = 0
exclude_val = None

def process_json(s):
    global result
    result = 0
    j = json.loads(s)

    traverse(j)
    return result

def traverse(obj):
    global result
    global exclude_val

    if isinstance(obj, dict):
        exclude = False
        if exclude_val:
            for k, v in obj.items():
                if v == exclude_val:
                    exclude = True
        if not exclude:
            return {k: traverse(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [traverse(elem) for elem in obj]
    else:
        try:
            result += int(obj)  # no container, just values
        except ValueError:
            pass


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
