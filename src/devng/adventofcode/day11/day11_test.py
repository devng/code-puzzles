#!/usr/bin/env python

from day11 import *
import unittest

class Day11Test(unittest.TestCase):

    def test_increment_string(self):
        s = increment_string("")
        self.assertEqual(s, "")

        s = increment_string("zdf")
        self.assertEqual(s, "zdg")

        s = increment_string("fdz")
        self.assertEqual(s, "fea")

        s = increment_string("zzz")
        self.assertEqual(s, "aaa")

        s = increment_string("zzziqwert")
        self.assertEqual(s, "zzzjaaaaa")

        s = increment_string("zzzzzzziok")
        self.assertEqual(s, "zzzzzzzipa")


    def test_is_password_valid(self):
        r = is_password_valid("abcdffaa")
        self.assertTrue(r)

        r = is_password_valid("ghjaabcc")
        self.assertTrue(r)

        r = is_password_valid("hijklmmn")
        self.assertFalse(r)

        r = is_password_valid("abbceffg")
        self.assertFalse(r)

        r = is_password_valid("abbcegjk")
        self.assertFalse(r)


    def test_next_valid_password(self):
        p = next_valid_password("abcdefgh")
        self.assertEqual(p, "abcdffaa")

        p = next_valid_password("ghijklmn")
        self.assertEqual(p, "ghjaabcc")
        pass


if __name__ == "__main__":
    unittest.main()
