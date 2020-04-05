#!/usr/bin/env python

from day05 import *
import unittest

class Day05Test(unittest.TestCase):

    def test_contains_naughty_chars(self):
        b1 = contains_naughty_chars("haegwjzuvuyypxyu")
        self.assertTrue(b1)

        b2 = contains_naughty_chars("ugknbfddgicrmopn")
        self.assertFalse(b2)


    def test_count_vowels(self):
        c1 = count_vowels("ugknbfddgicrmopn")
        self.assertEqual(c1, 3)

        c2 = count_vowels("dvszwmarrgswjxmb")
        self.assertEqual(c2, 1)

        c3 = count_vowels("bcvfd")
        self.assertEqual(c3, 0)


    def test_has_letter_sequence(self):
        b1 = has_letter_sequence("ugknbfddgicrmopn")
        self.assertTrue(b1)

        b2 = has_letter_sequence("jchzalrnumimnmhp")
        self.assertFalse(b2)


    def test_has_mirror_letters(self):
        b1 = has_mirror_letters("aaa")
        self.assertTrue(b1)

        b2 = has_mirror_letters("abcdefeghi")
        self.assertTrue(b2)

        b3 = has_mirror_letters("qwerty")
        self.assertFalse(b3)

    def test_has_non_overlapping_pairs(self):
        b1 = has_non_overlapping_pairs("xyxy")
        self.assertTrue(b1)

        b2 = has_non_overlapping_pairs("aaa")
        self.assertFalse(b2)

        b3 = has_non_overlapping_pairs("aabcdefgaa")
        self.assertTrue(b3)


    def test_check_word(self):
        is_nice = check_word("ugknbfddgicrmopn")
        self.assertTrue(is_nice)

        is_nice = check_word("aaa")
        self.assertTrue(is_nice)

        is_nice = check_word("jchzalrnumimnmhp")
        self.assertFalse(is_nice)

        is_nice = check_word("haegwjzuvuyypxyu")
        self.assertFalse(is_nice)

        is_nice = check_word("dvszwmarrgswjxmb")
        self.assertFalse(is_nice)


    def test_check_word_2(self):
        is_nice = check_word_2("qjhvhtzxzqqjkmpb")
        self.assertTrue(is_nice)

        is_nice = check_word_2("aaa")
        self.assertFalse(is_nice)

        is_nice = check_word_2("xxyxx")
        self.assertTrue(is_nice)

        is_nice = check_word_2("uurcxstgmygtbstg")
        self.assertFalse(is_nice)

        is_nice = check_word_2("ieodomkazucvgmuy")
        self.assertFalse(is_nice)


if __name__ == "__main__":
    unittest.main()
