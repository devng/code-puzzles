#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals


def parse_file(filename):
    grid = []
    with open(filename, "r") as fin:
        for line in fin:
            r = []
            for ch in line:
                if ch == "#":
                    r.append(True)
                elif ch == ".":
                    r.append(False)
            grid.append(r)
    return grid


def get_neighbors(x, y, grid):
    for i in range(-1, 2):
        x_n = x + i
        if x_n < 0 or x_n >= len(grid):
            continue
        for j in range(-1, 2):
            y_n = y + j
            if y_n < 0 or y_n >= len(grid[x_n]):
                continue
            if x_n == x and y_n == y:
                continue
            yield x_n, y_n


def count_lights(grid):
    c = 0
    for x in grid:
        for y in x:
            if y:
                c += 1
    return c


def count_lit_neighbors(x, y, grid):
    c = 0
    for n in get_neighbors(x, y, grid):
        if grid[n[0]][n[1]]:
            c += 1
    return c


def next_state(grid, corners_on=False):
    size = len(grid)
    new_grid = [[False for _ in range(size)] for _ in range(size)]

    for x in range(size):
        for y in range(size):
            val = grid[x][y]
            count = count_lit_neighbors(x, y, grid)
            next_val = False
            if val and (count == 2 or count == 3):
                next_val = True
            elif not val and count == 3:
                next_val = True
            new_grid[x][y] = next_val
    if corners_on:
        corners_lights_on(new_grid)
    # print_grid(new_grid) # DEBUG
    return new_grid


def corners_lights_on(grid):
    size = len(grid)
    grid[0][0] = True
    grid[0][size-1] = True
    grid[size-1][0] = True
    grid[size-1][size-1] = True


def print_grid(grid):
    print("Grid:")
    for l in grid:
        l_s = map(lambda b: "#" if b else ".", l)
        for s in l_s:
            print(s, end="")
        print()


def solution_part1():
    grid = parse_file("input.txt")
    for i in range(100):
        grid = next_state(grid)
    lights = count_lights(grid)
    print("Answer part one: %d" % lights)


def solution_part2():
    grid = parse_file("input.txt")
    corners_lights_on(grid)
    for i in range(100):
        grid = next_state(grid, True)
    lights = count_lights(grid)
    print("Answer part two: %d" % lights)


if __name__ == "__main__":
    solution_part1()
    solution_part2()
