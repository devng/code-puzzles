#!/usr/bin/env python3

import pascal_walk as pw
import unittest

class PascalWalkTest(unittest.TestCase):
    def test_solve(self):
        pw.DEBUG = True
        for n in range(1, 1002):
            print("Solving pascal path for N =", n)
            pw.solve(n)


if __name__ == '__main__':
    unittest.main()
