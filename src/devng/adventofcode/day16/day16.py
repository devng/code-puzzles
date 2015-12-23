#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

import re

MFCSAM_FACTS = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

FILENAME = "input.txt"

line_regex = re.compile(r"Sue (\d+): (.*)")


def check_aunt(d):
    for k, v in d.items():
        if k in MFCSAM_FACTS:
            if v != MFCSAM_FACTS[k]:
                return False
    return True


def check_aunt2(d):
    for k, v in d.items():
        if k in MFCSAM_FACTS:
            if k in ["cats", "trees"]:
                if v <= MFCSAM_FACTS[k]:
                    return False
            elif k in ["pomeranians", "goldfish"]:
                if v >= MFCSAM_FACTS[k]:
                    return False
            else:
                if v != MFCSAM_FACTS[k]:
                    return False
    return True


def parse_line(line):
    m = line_regex.match(line)
    val_dict = {}
    aunt_id = 0
    if m:
        aunt_id = int(m.group(1))
        vals = m.group(2).split(",")
        for val in vals:
            v = val.split(":")
            val_dict[v[0].strip()] = int(v[1].strip())
    else:
        raise ValueError("Invalid line: " + line)
    return aunt_id, val_dict


def main():
    aunt_id1 = 0
    aunt_id2 = 0
    with open(FILENAME, "r") as f:
        for line in f:
            aid, vdict = parse_line(line)
            if check_aunt(vdict):
                aunt_id1 = aid
            if check_aunt2(vdict):
                aunt_id2 = aid
    print("Answer part one: %s\nAnswer part two: %s" % (aunt_id1, aunt_id2))


if __name__ == "__main__":
    main()
