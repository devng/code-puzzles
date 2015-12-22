#!/usr/bin/env python

import day15
import unittest


class Day15Test(unittest.TestCase):

    def test_compute_score(self):
        day15.ingredients = (
            ("Butterscotch", -1, -2, 6, 3, 8),
            ("Cinnamon", 2, 3, -2, -1, 3)
        )
        r = day15.compute_score((44, 56))
        self.assertEqual(r, (62842880, 520))

        r = day15.compute_score((40, 60))
        self.assertEqual(r, (57600000, 500))


if __name__ == "__main__":
    unittest.main()
