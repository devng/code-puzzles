#!/usr/bin/env python

import day13
import unittest

class Day13Test(unittest.TestCase):

    def test_parse_file(self):
        day13.parse_file("input_test.txt")
        expected_dict = {
            ('Bob', 'David'): -63,
            ('Carol', 'David'): 55,
            ('David', 'Alice'): 46,
            ('Bob', 'Carol'): -7,
            ('Alice', 'Bob'): 54,
            ('Alice', 'David'): -2,
            ('Alice', 'Carol'): -79,
            ('Carol', 'Bob'): 60,
            ('David', 'Carol'): 41,
            ('Bob', 'Alice'): 83,
            ('Carol', 'Alice'): -62,
            ('David', 'Bob'): -7
        }
        expected_set = set(['Bob', 'David', 'Alice', 'Carol'])
        self.assertEqual(day13.happiness_dict, expected_dict)
        self.assertEqual(day13.guests, expected_set)


    def test_compute_hapiness(self):
        day13.happiness_dict = expected_dict = {
            ('Bob', 'David'): -63,
            ('Carol', 'David'): 55,
            ('David', 'Alice'): 46,
            ('Bob', 'Carol'): -7,
            ('Alice', 'Bob'): 54,
            ('Alice', 'David'): -2,
            ('Alice', 'Carol'): -79,
            ('Carol', 'Bob'): 60,
            ('David', 'Carol'): 41,
            ('Bob', 'Alice'): 83,
            ('Carol', 'Alice'): -62,
            ('David', 'Bob'): -7
        }
        day13.guests = expected_set = set(['Bob', 'David', 'Alice', 'Carol'])
        r = day13.compute_hapiness(['Bob', 'Carol', 'David', 'Alice',])
        self.assertEqual(r, 330)


    def test_find_best_seating_arrangement(self):
        h = day13.find_best_seating_arrangement("input_test.txt")
        self.assertEqual(h, 330)


if __name__ == "__main__":
    unittest.main()
