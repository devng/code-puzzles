#!/usr/bin/env python

from day06 import *
import unittest

class Day06Test(unittest.TestCase):
    def test_init_grid(self):
        grid = init_grid(2)
        expected = [[False, False], [False, False]]
        self.assertEqual(grid, expected)

        grid = init_grid(1)
        expected = [[False]]
        self.assertEqual(grid, expected)

        grid = init_grid(2, 0)
        expected = [[0, 0], [0, 0]]
        self.assertEqual(grid, expected)

        grid = init_grid(1, val=0)
        expected = [[0]]
        self.assertEqual(grid, expected)


    def test_count_lights(self):
        grid =[[False, False], [False, False]]
        count = count_lights(grid)
        self.assertEqual(count, 0)

        grid = [[False, True], [True, False]]
        count = count_lights(grid)
        self.assertEqual(count, 2)

        grid = [[False, True], [True, False], [True, True]]
        count = count_lights(grid)
        self.assertEqual(count, 4)


    def test_grid_action(self):
        grid = [[False, True, False], [False, False, False], [True, False, False]]
        grid_action(grid, "turn on", 0, 0, 2, 2)
        expected = [[True, True, True], [True, True, True], [True, True, True]]
        self.assertEqual(grid, expected)

        grid = [[False, True, False], [False, True, False], [False, False, False]]
        grid_action(grid, "turn off", 0, 0, 2, 2)
        expected = [[False, False, False], [False, False, False], [False, False, False]]
        self.assertEqual(grid, expected)

        grid = [[False, True, False], [False, True, False], [False, False, False]]
        grid_action(grid, "toggle", 0, 0, 2, 2)
        expected = [[True, False, True], [True, False, True], [True, True, True]]
        self.assertEqual(grid, expected)

        grid = [[False, False, False], [False, False, False], [False, False, False]]
        grid_action(grid, "turn on", 1, 0, 2, 1)
        expected = [[False, False, False], [True, True, False], [True, True, False]]
        self.assertEqual(grid, expected)

        grid = [[False, True, False], [True, True, True], [True, True, False]]
        grid_action(grid, "turn off", 1, 1, 2, 2)
        expected = [[False, True, False], [True, False, False], [True, False, False]]
        self.assertEqual(grid, expected)

        grid = [[False, True, False], [True, True, True], [True, True, False]]
        grid_action(grid, "toggle", 0, 0, 2, 0)
        expected = [[True, True, False], [False, True, True], [False, True, False]]
        self.assertEqual(grid, expected)


    def test_brightness_grid_action(self):
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        brightness_grid_action(grid, "toggle", 0, 0, 2, 2)
        expected = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.assertEqual(grid, expected)

        grid = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        brightness_grid_action(grid, "turn off", 0, 1, 1, 2)
        expected = [[2, 1, 1], [2, 1, 1], [2, 2, 2]]
        self.assertEqual(grid, expected)

        grid = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        brightness_grid_action(grid, "turn on", 0, 1, 1, 2)
        expected = [[2, 3, 3], [2, 3, 3], [2, 2, 2]]
        self.assertEqual(grid, expected)


    def test_count_brightness(self):
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        b = count_brightness(grid)
        self.assertEqual(b, 0)

        grid = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        b = count_brightness(grid)
        self.assertEqual(b, 18)

        grid = [[2, 3, 3], [2, 3, 3], [0, 1, 2]]
        b = count_brightness(grid)
        self.assertEqual(b, 19)


    def test_parse_line(self):
        r = parse_line("turn on 0,0 through 999,999")
        self.assertEqual(r, ("turn on", 0, 0, 999, 999))

        r = parse_line("toggle 0,0 through 999,0")
        self.assertEqual(r, ("toggle", 0, 0, 999, 0))

        r = parse_line("turn off 499,499 through 500,500")
        self.assertEqual(r, ("turn off", 499, 499, 500, 500))



if __name__ == "__main__":
    unittest.main()
