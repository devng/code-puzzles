#!/usr/bin/env python

from day02 import *
import unittest

class Day02Test(unittest.TestCase):
    def test_calc_sufface_area(self):
        a1 = calc_sufface_area(2, 3, 4)
        self.assertEqual(a1, 52)

        a2 = calc_sufface_area(1, 1, 10)
        self.assertEqual(a2, 42)

    def test_calc_smallest_side_area(self):
        s1 = calc_smallest_side_area(2, 3, 4)
        self.assertEqual(s1, 6)

        s2 = calc_smallest_side_area(10, 1, 1)
        self.assertEqual(s2, 1)

    def test_calc_needed_paper(self):
        p1 = calc_needed_paper(2, 3, 4)
        self.assertEqual(p1, 58)

        p2 = calc_needed_paper(1, 1, 10)
        self.assertEqual(p2, 43)

    def test_parse_dims(self):
        a1 = parse_dims("2x3x4")
        self.assertEqual(a1, [2, 3, 4])

        a2 = parse_dims("1x1x10")
        self.assertEqual(a2, [1, 1, 10])

    def test_calc_ribbon(self):
        r1 = calc_ribbon(2, 3, 4)
        self.assertEqual(r1, 34)

        r2 = calc_ribbon(1, 1, 10)
        self.assertEqual(r2, 14)

if __name__ == '__main__':
    unittest.main()
