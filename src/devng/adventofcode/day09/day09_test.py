#!/usr/bin/env python

import day09
import unittest

class Day09Test(unittest.TestCase):

    def test_parse_line(self):
        day09.parse_line("Dublin to Belfast = 141")
        day09.parse_line("London to Belfast = 518")
        day09.parse_line("London to Dublin = 464")
        expected_cities = set(["Dublin", "Belfast", "London"])
        self.assertEqual(expected_cities, day09.cities)

        expected_distances = {
            ("Dublin", "Belfast"): 141,
            ("London", "Belfast"): 518,
            ("London", "Dublin"): 464
        }
        self.assertEqual(expected_distances, day09.distances)


    def test_find_route(self):
        day09.cities = set(["Dublin", "Belfast", "London"])
        day09.distances = {
            ("Dublin", "Belfast"): 141,
            ("London", "Belfast"): 518,
            ("London", "Dublin"): 464
        }
        r = day09.find_route()
        self.assertEqual(r, (605, 982))


    def test_process_file(self):
        r = day09.process_file("input_test.txt")
        self.assertEqual(r, (605, 982))


if __name__ == "__main__":
    unittest.main()
