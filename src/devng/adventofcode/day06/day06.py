#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

import re

line_regex = re.compile(r"(\D*) (\d*),(\d*) through (\d*),(\d*)")

# Actions
TON = "turn on"
TOFF = "turn off"
TOGG = "toggle"


def init_grid(size, val=False):
    return [[val for _ in range(size)] for _ in range(size)]


def count_lights(grid):
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y]:
                count += 1
    return count


def count_brightness(grid):
    return sum(sum(x) for x in grid)


def grid_action(grid, action, start_x, start_y, end_x, end_y):
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if action == TON:
                grid[x][y] = True
            elif action == TOFF:
                grid[x][y] = False
            elif action == TOGG:
                grid[x][y] = not grid[x][y]
            else:
                print("Unknown action: " + action)


def brightness_grid_action(grid, action, start_x, start_y, end_x, end_y):
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if action == TON:
                grid[x][y] = grid[x][y] + 1
            elif action == TOFF:
                grid[x][y] = max(grid[x][y] - 1, 0) # do not go bellow 0
            elif action == TOGG:
                grid[x][y] = grid[x][y] + 2
            else:
                print("Unknown action: " + action)


def parse_line(line):
    m = line_regex.match(line)
    if m:
        action = m.group(1)
        start_x = int(m.group(2))
        start_y = int(m.group(3))
        end_x = int(m.group(4))
        end_y = int(m.group(5))
        return action, start_x, start_y, end_x, end_y
    else:
        print("Invalid line: " + line)
        return None


def main():
    grid = init_grid(1000)
    b_grid = init_grid(1000, val=0)
    with open("input.txt", "r") as fin:
        for line in fin:
            action, start_x, start_y, end_x, end_y = parse_line(line)
            grid_action(grid, action, start_x, start_y, end_x, end_y)
            brightness_grid_action(b_grid, action, start_x, start_y, end_x, end_y)
    print("Answer part one: ", count_lights(grid))
    print("Answer part two: ", count_brightness(b_grid))


if __name__ == "__main__":
    main()
