#!/usr/bin/env python
# coding: utf-8

import itertools
import unittest

def string_permutations(str):
    def string_permutations_generator(str):
        for s in itertools.permutations(sorted(str), len(str)):
            yield ''.join(s)
    return ','.join(string_permutations_generator(str))

class StringPermutationsTest(unittest.TestCase):
    def test_string_permutations(self):
        s0 = string_permutations('hat')
        self.assertEqual(s0, 'aht,ath,hat,hta,tah,tha')

        s1 = string_permutations('Zu6')
        self.assertEqual(s1, '6Zu,6uZ,Z6u,Zu6,u6Z,uZ6')

if __name__ == '__main__':
    unittest.main()
