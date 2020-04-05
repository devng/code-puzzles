#!/usr/bin/env python

from day03 import *
import unittest


class Day03Test(unittest.TestCase):

    def test_move(self):
        x1, y1 = move(2, 3, "^")
        self.assertEqual(x1, 2)
        self.assertEqual(y1, 4)

        x2, y2 = move(2, 3, ">")
        self.assertEqual(x2, 3)
        self.assertEqual(y2, 3)

        x3, y3 = move(2, 3, "v")
        self.assertEqual(x3, 2)
        self.assertEqual(y3, 2)

        x4, y4 = move(2, 3, "<")
        self.assertEqual(x4, 1)
        self.assertEqual(y4, 3)

        x5, y5 = move(2, 3, "aa")
        self.assertEqual(x5, 2)
        self.assertEqual(y5, 3)


    def test_count_houses(self):
        c1 = count_houses(">")
        self.assertEqual(c1, 2)

        c2 = count_houses("^>v<")
        self.assertEqual(c2, 4)

        c3 = count_houses("^v^v^v^v^v")
        self.assertEqual(c3, 2)


    def test_count_houses_2(self):
        c1 = count_houses_2("^v")
        self.assertEqual(c1, 3)

        c2 = count_houses_2("^>v<")
        self.assertEqual(c2, 3)

        c3 = count_houses_2("^v^v^v^v^v")
        self.assertEqual(c3, 11)


if __name__ == "__main__":
    unittest.main()
