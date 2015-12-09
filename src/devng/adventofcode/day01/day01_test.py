#!/usr/bin/env python

from day01 import *
import unittest

class Day01Test(unittest.TestCase):
    def test_count_floor(self):
        f1 = count_floor("(())")
        self.assertEqual(f1, 0)

        f2 = count_floor("))(((((")
        self.assertEqual(f2, 3)

        f3 = count_floor(")())())")
        self.assertEqual(f3, -3)

    def test_find_basement(self):
        b1 = find_basement(")")
        self.assertEqual(b1, 1)

        b2 = find_basement("()())")
        self.assertEqual(b2, 5)

if __name__ == '__main__':
    unittest.main()
