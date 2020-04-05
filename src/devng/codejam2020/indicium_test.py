#!/usr/bin/env python3
# coding: utf-8

from indicium import *
import time
import unittest

class IndiciumTest(unittest.TestCase):
    def test_find_matrix(self):
        s, m = find_matrix(3, 6)
        self.assertEqual(s, "POSSIBLE", False)
        self.assertListEqual(m, [[2, 1, 3], [3, 2, 1], [1, 3, 2]])

        s, m = find_matrix(2, 3, False)
        self.assertEqual(s, "IMPOSSIBLE")
        self.assertEqual(m, None)


    def test_perforamnce(self):
        for n in range(2, 6):
            max_k = n**2 + 1
            for k in range(n, max_k):
                start_time = time.time()
                print("Running performance test n = {}, k = {}".format(n, k))
                s, m = find_matrix(n, k, False)
                elapsed_time = time.time() - start_time
                print("    Elapsed time: {:.4f}, solution: {}".format(elapsed_time, s))
                if (elapsed_time > 0.5):
                    print("    SLOW CASE solution matrix:", m)


if __name__ == '__main__':
    unittest.main()
