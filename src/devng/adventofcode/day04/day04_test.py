#!/usr/bin/env python

from day04 import *
import unittest


class Day04Test(unittest.TestCase):

    def test_check_num(self):
        b1 = check_num("abcdef", 609043)
        self.assertTrue(b1)

        b2 = check_num("abcdef", 609)
        self.assertFalse(b2)

        b3 = check_num("pqrstuv", 1048970)
        self.assertTrue(b3)

        b4 = check_num("pqrstuv", 104897)
        self.assertFalse(b4)

        b5 = check_num("iwrupvqb", 9958218, "000000")
        self.assertTrue(b5)


    def test_check_range(self):
        n1 = check_range("abcdef", 609040, 609045)
        self.assertEqual(n1, 609043)

        n2 = check_range("abcdef")
        self.assertEqual(n2, None)

        n3 = check_range("iwrupvqb", 9958210, 10, "000000")
        self.assertEqual(n3, 9958218)


if __name__ == "__main__":
    unittest.main()
