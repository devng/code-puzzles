#!/usr/bin/env python


from day10 import *
import unittest


class Day10Test(unittest.TestCase):
    def test_look_and_say(self):
        r = look_and_say("1")
        self.assertEqual(r, "11")

        r = look_and_say("11")
        self.assertEqual(r, "21")

        r = look_and_say("1211")
        self.assertEqual(r, "111221")

        r = look_and_say("111221")
        self.assertEqual(r, "312211")


if __name__ == "__main__":
    unittest.main()
