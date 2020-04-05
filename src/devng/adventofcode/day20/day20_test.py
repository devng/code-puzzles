#!/usr/bin/env python

from day20 import *
import unittest


class Day20Test(unittest.TestCase):

    def test_find_house(self):
        r = find_house(150)
        self.assertEqual(r, 8)

        r = find_house(150, 2, 5)
        self.assertEqual(r, 36)


if __name__ == "__main__":
    unittest.main()
