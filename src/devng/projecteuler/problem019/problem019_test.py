#!/usr/bin/env python
# coding: utf-8

from problem019 import count_sundays
import unittest


class Problem019Test(unittest.TestCase):
    def test_count_sundays(self):
        sundays = count_sundays(2015, 2016)
        self.assertEqual(sundays, 3)

        sundays = count_sundays(1901, 2001)
        self.assertEqual(sundays, 171)

if __name__ == '__main__':
    unittest.main()
