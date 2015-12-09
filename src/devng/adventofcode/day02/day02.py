#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

def calc_sufface_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l


def calc_smallest_side_area(l, w, h):
    a = sorted([l, w, h])
    return a[0] * a[1]


def parse_dims(dim_str):
    return [int(s) for s in dim_str.split('x')]


def calc_needed_paper(l, w, h):
    a = calc_sufface_area(l, w, h)
    b = calc_smallest_side_area(l, w, h)
    # print(a, b) # debug
    return a + b

def calc_ribbon(l, w, h):
    a = sorted([l, w, h])
    r = a[0] + a[0] + a[1] + a[1]
    r += l * w * h
    return r

def calc_ribbon_bow(l, w, h):
    return

def main():
    total_paper = 0
    total_ribbon = 0
    with open("input.txt", 'r') as fin:
        for line in fin:
             dims = parse_dims(line)
             total_paper += calc_needed_paper(dims[0], dims[1], dims[2])
             total_ribbon += calc_ribbon(dims[0], dims[1], dims[2])

    print("Answer part one: ", total_paper)
    print("Answer part two: ", total_ribbon)


if __name__ == "__main__":
    main()
