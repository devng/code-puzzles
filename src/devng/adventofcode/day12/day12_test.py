#!/usr/bin/env python


import day12
import unittest


class Day12Test(unittest.TestCase):
    def test_process_json(self):
        day12.result = 0
        day12.process_json("{}")
        self.assertEqual(day12.result, 0)

        day12.result = 0
        day12.process_json("[1,2,3]")
        self.assertEqual(day12.result, 6)

        day12.result = 0
        day12.process_json('{"a":2,"b":4}')
        self.assertEqual(day12.result, 6)

        day12.result = 0
        day12.process_json('{"a":{"b":4},"c":-1}')
        self.assertEqual(day12.result, 3)

        day12.result = 0
        day12.process_json('{"a":{"b":4},"c":-1}')
        self.assertEqual(day12.result, 3)

        day12.result = 0
        day12.process_json('[-1,{"a":1}]')
        self.assertEqual(day12.result, 0)


    def test_process_json_with_exclude(self):
        day12.exclude_val = "red"

        day12.result = 0
        day12.process_json("[1,2,3]")
        self.assertEqual(day12.result, 6)

        day12.result = 0
        day12.process_json('[1,{"c":"red","b":2},3]')
        self.assertEqual(day12.result, 4)

        day12.result = 0
        day12.process_json('[1,"red",5]')
        self.assertEqual(day12.result, 6)


if __name__ == "__main__":
    unittest.main()
