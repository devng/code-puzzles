#!/usr/bin/env python

from day08 import *
import unittest


class Day08Test(unittest.TestCase):
    def test_process_file(self):
        r = process_file("input_test.txt")
        self.assertEqual(r, (12, 19))


if __name__ == "__main__":
    unittest.main()
