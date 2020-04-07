#!/usr/bin/env python3

from whole_new_word import *
import unittest

class NestingDepthTest(unittest.TestCase):
    def test_find_word(self):
        words = ["AA", "AB", "BA", "BB"]
        w = find_word(words, 4, 2)
        self.assertEqual(w, "-")

        words = ["CAKE", "TORN", "SHOW"]
        w = find_word(words, 3, 4)
        self.assertNotEqual(w, "-")

if __name__ == '__main__':
    unittest.main()
