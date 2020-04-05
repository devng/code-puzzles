#!/usr/bin/env python

from day16 import *
import unittest

class Day16Test(unittest.TestCase):

    def test_parse_line(self):
        aid, vdict = parse_line("Sue 32: pomeranians: 10, vizslas: 5, goldfish: 5")
        expected_id = 32
        expected_vdict = {
            "pomeranians": 10,
            "vizslas": 5,
            "goldfish": 5
        }
        self.assertEqual(aid, expected_id)
        self.assertEqual(vdict, expected_vdict)


    def test_check_aunt(self):
        aunt_dict = {
            "pomeranians": 10,
            "vizslas": 5,
            "goldfish": 5
        }
        b = check_aunt(aunt_dict)
        self.assertFalse(b)

        aunt_dict = {
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0
        }
        b = check_aunt(aunt_dict)
        self.assertTrue(b)


    def test_check_aunt2(self):
        aunt_dict = {
            "pomeranians": 10,
            "vizslas": 5,
            "goldfish": 5
        }
        b = check_aunt(aunt_dict)
        self.assertFalse(b)

        aunt_dict = {
            "samoyeds": 2,
            "pomeranians": 3,
            "trees:": 2,
            "goldfish": 5
        }
        b = check_aunt(aunt_dict)
        self.assertTrue(b)



if __name__ == "__main__":
    unittest.main()
