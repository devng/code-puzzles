#!/usr/bin/env python3
# coding: utf-8

from nesting_depth import *
import unittest

class NestingDepthTest(unittest.TestCase):
    def test_insert_parentheses(self):
        s = insert_parentheses([0])
        self.assertEqual(s, "0")

        s = insert_parentheses([0, 0, 0, 0])
        self.assertEqual(s, "0000")

        s = insert_parentheses([1, 0, 1])
        self.assertEqual(s, "(1)0(1)")

        s = insert_parentheses([1, 1, 1, 0, 0, 0])
        self.assertEqual(s, "(111)000")

        s = insert_parentheses([1])
        self.assertEqual(s, "(1)")

        s = insert_parentheses([0, 2, 1])
        self.assertEqual(s, "0((2)1)")

        s = insert_parentheses([3, 1, 2])
        self.assertEqual(s, "(((3))1(2))")

        s = insert_parentheses([4])
        self.assertEqual(s, "((((4))))")

        s = insert_parentheses([2, 2, 1])
        self.assertEqual(s, "((22)1)")


if __name__ == '__main__':
    unittest.main()
