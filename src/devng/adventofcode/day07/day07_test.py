#!/usr/bin/env python3

from day07 import *
import unittest


class Day07Test(unittest.TestCase):
    def test_process_file(self):
        expected_vars = {
            "d": 72,
            "e": 507,
            "f": 492,
            "g": 114,
            "h": 65412,
            "i": 65079,
            "x": 123,
            "y": 456
        }

        actual_var_i = process_file("input_test.txt", "i")
        self.assertEqual(actual_var_i, expected_vars['i'])

        actual_var_e = process_file("input_test.txt", "e")
        self.assertEqual(actual_var_e, expected_vars['e'])

        actual_var_x = process_file("input_test.txt", "x")
        self.assertEqual(actual_var_x, expected_vars['x'])

        actual_var_h = process_file("input_test.txt", "h")
        self.assertEqual(actual_var_h, expected_vars['h'])


if __name__ == "__main__":
    unittest.main()
