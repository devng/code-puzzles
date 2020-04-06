#!/usr/bin/env python3
# coding: utf-8

from vestigium import *
import unittest

test_input_1 = """
    1 2 3 4
    2 1 4 3
    3 4 1 2
    4 3 2 1
""".strip().split('\n')

test_input_2 = """
    2 2 2 2
    2 3 2 3
    2 2 2 3
    2 2 2 2
""".strip().split('\n')

test_input_3 = """
    2 1 3
    1 3 2
    1 2 3
""".strip().split('\n')

class VestigiumTest(unittest.TestCase):
    def test_parse_matrix_input(self):
        case_matrix_1 = parse_matrix_input(test_input_1)
        self.assertListEqual(case_matrix_1,
            [[1, 2, 3, 4], [2, 1, 4, 3], [3, 4, 1, 2], [4, 3, 2, 1]])

        case_matrix_2 = parse_matrix_input(test_input_2)
        self.assertListEqual(case_matrix_2,
            [[2, 2, 2, 2], [2, 3, 2, 3], [2, 2, 2, 3], [2, 2, 2, 2]])

        case_matrix_3 = parse_matrix_input(test_input_3)
        self.assertListEqual(case_matrix_3, [[2, 1, 3], [1, 3, 2], [1, 2, 3]])

    def test_check_case(self):
        case_matrix_1 = parse_matrix_input(test_input_1)
        self.assertSequenceEqual(check_case(case_matrix_1), (4, 0, 0))

        case_matrix_2 = parse_matrix_input(test_input_2)
        self.assertSequenceEqual(check_case(case_matrix_2), (9, 4, 4))

        case_matrix_3 = parse_matrix_input(test_input_3)
        self.assertSequenceEqual(check_case(case_matrix_3), (8, 0, 2))


if __name__ == '__main__':
    unittest.main()
