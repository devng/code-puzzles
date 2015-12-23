#!/usr/bin/env python

import day18
import unittest


class Day18Test(unittest.TestCase):

    def test_get_neighbors(self):
        grid = [
            [True, True, True, False, False],
            [False, False, False, True, True]
        ]
        r = [(x, y) for x, y in day18.get_neighbors(0, 1, grid)]
        self.assertEqual(len(r), 5)
        self.assertEqual(r, [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)])

        grid = [
            [True, True, False],
            [False, False, False],
            [False, False, True]
        ]
        r = [(x, y) for x, y in day18.get_neighbors(1, 1, grid)]
        self.assertEqual(len(r), 8)
        self.assertEqual(r, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2),])


    def test_parse_file(self):
        grid = day18.parse_file("input_test.txt")
        expected_grid = [
            [False, True, False, True, False, True],
            [False, False, False, True, True, False],
            [True, False, False, False, False, True],
            [False, False, True, False, False, False],
            [True, False, True, False, False, True],
            [True, True, True, True, False, False]
        ]
        self.assertEqual(grid, expected_grid)


    def test_next_state(self):
        grid = [
            [False, True, False, True, False, True],
            [False, False, False, True, True, False],
            [True, False, False, False, False, True],
            [False, False, True, False, False, False],
            [True, False, True, False, False, True],
            [True, True, True, True, False, False]
        ]

        # Test after 1 step
        expected_grid = [
            [False, False, True, True, False, False],
            [False, False, True, True, False, True],
            [False, False, False, True, True, False],
            [False, False, False, False, False, False],
            [True, False, False, False, False, False],
            [True, False, True, True, False, False]
        ]


        r = day18.next_state(grid)
        self.assertEqual(r, expected_grid)

        # Test after 4 steps
        expected_grid = [
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, True, True, False, False],
            [False, False, True, True, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False]
        ]

        r = day18.next_state(r)
        r = day18.next_state(r)
        r = day18.next_state(r)
        self.assertEqual(r, expected_grid)


    def test_next_state_part2(self):
        grid = [
            [True, True, False, True, False, True],
            [False, False, False, True, True, False],
            [True, False, False, False, False, True],
            [False, False, True, False, False, False],
            [True, False, True, False, False, True],
            [True, True, True, True, False, True]
        ]


        # Test after 1 step
        expected_grid = [
            [True, False, True, True, False, True],
            [True, True, True, True, False, True],
            [False, False, False, True, True, False],
            [False, False, False, False, False, False],
            [True, False, False, False, True, False],
            [True, False, True, True, True, True]
        ]

        r = day18.next_state(grid, True)
        self.assertEqual(r, expected_grid)


        # Test after 5 steps
        expected_grid = [
            [True, True, False, True, True, True],
            [False, True, True, False, False, True],
            [False, True, True, False, False, False],
            [False, True, True, False, False, False],
            [True, False, True, False, False, False],
            [True, True, False, False, False, True]
        ]
        for i in range(4):
            r = day18.next_state(r, True)
        self.assertEqual(r, expected_grid)


    def test_count_lit_neighbors(self):
        grid = [
            [True, True, True, False, False],
            [False, False, False, True, True]
        ]
        r = day18.count_lit_neighbors(0, 0, grid)
        self.assertEqual(r, 1)

        r = day18.count_lit_neighbors(0, 4, grid)
        self.assertEqual(r, 2)

        r = day18.count_lit_neighbors(0, 2, grid)
        self.assertEqual(r, 2)


    def test_count_lights(self):
        grid = [
            [True, True, True, False, False],
            [False, False, False, True, True]
        ]
        r = day18.count_lights(grid)
        self.assertEqual(r, 5)

        grid = [
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, True, True, False, False],
            [False, False, True, True, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False]
        ]
        r = day18.count_lights(grid)
        self.assertEqual(r, 4)


        grid = [
            [True, True, False, True, True, True],
            [False, True, True, False, False, True],
            [False, True, True, False, False, False],
            [False, True, True, False, False, False],
            [True, False, True, False, False, False],
            [True, True, False, False, False, True]
        ]
        r = day18.count_lights(grid)
        self.assertEqual(r, 17)


if __name__ == "__main__":
    unittest.main()
