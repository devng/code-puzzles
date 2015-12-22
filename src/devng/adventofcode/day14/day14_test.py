#!/usr/bin/env python

from day14 import *
import unittest

class Day13Test(unittest.TestCase):

    def test_race_distance(self):
        # Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
        d = race_distance(11, 14, 10, 127)
        self.assertEqual(d, 140)

        d = race_distance(138, 14, 10, 127)
        self.assertEqual(d, 154)

        d = race_distance(1000, 14, 10, 127)
        self.assertEqual(d, 1120)

        # Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
        d = race_distance(1000, 16, 11, 162)
        self.assertEqual(d, 1056)


    def test_all_distances(self):
        duration = 1000
        reindeer_dict = {
            "Comet": (14, 10, 127),
            "Dancer": (16, 11, 162)
        }

        d = all_distances(duration, reindeer_dict)

        expected_d = [
            ("Comet", 1120),
            ("Dancer", 1056)
        ]

        self.assertEqual(d, expected_d)


    def test_all_points(self):
        duration = 1000
        reindeer_dict = {
            "Comet": (14, 10, 127),
            "Dancer": (16, 11, 162)
        }

        d = all_points(duration, reindeer_dict)

        expected_d = {
            "Comet": 312,
            "Dancer": 689
        }

        self.assertEqual(d, expected_d)


if __name__ == "__main__":
    unittest.main()
