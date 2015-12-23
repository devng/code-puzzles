#!/usr/bin/env python

import day17
import unittest


class Day17Test(unittest.TestCase):

    def test_parse_file(self):
        r = day17.parse_file("input_test.txt")
        self.assertEqual(r, [20, 15, 10, 5, 5])


    def test_find_solution_part1(self):
        day17.eggnog = 25
        r = day17.find_solution_part1([20, 15, 10, 5, 5])
        self.assertEqual(r, 4)

    def test_find_solution_part2(self):
        day17.eggnog = 25
        r = day17.find_solution_part2([20, 15, 10, 5, 5])
        self.assertEqual(r, 3) 


if __name__ == "__main__":
    unittest.main()
