#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

from collections import defaultdict


def contains_naughty_chars(s):
    """
    Returns True if the input string contains the sub-strings `ab`, `cd`, `pq`, or `xy`.
    """
    if ('ab' in s) or ('cd' in s) or ('pq' in s) or ('xy' in s):
        return True
    return False


def has_non_overlapping_pairs(s):
    """
    Returns True if it contains a pair of any two letters that appears at least twice
    in the string without overlapping, like `xyxy` (`xy`) or `aabcdefgaa` (`aa`),
    but not like `aaa` (`aa`, but it overlaps).
    """
    pairs_count = defaultdict(int)
    for i in range(0, len(s)-1, 1):
        if i + 2 < len(s):
            if s[i] + s[i+1] != s[i+1] + s[i+2]:
                pairs_count[s[i] + s[i+1]] += 1
        else:
            if s[i] + s[i+1] != s[i-1] + s[i]:
                pairs_count[s[i] + s[i+1]] += 1

    for count in pairs_count.values():
        if count >= 2:
            return True
    return False


def has_mirror_letters(s):
    """
    Returns True if the input word contains at least one letter which repeats with exactly
    one letter between them, like `xyx`, `abcdefeghi` (`efe`), or even `aaa`.
    """
    for i in range(0, len(s), 1):
        if i + 2 < len(s):
            if s[i] == s[i+2]:
                return True
        else:
            break
    return False



def count_vowels(s):
    """
    Returns the number of vowels in the input word s.
    """
    vowels = "aeiou"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


def has_letter_sequence(s):
    """
    Returns True if the input word s contains at least one letter that appears
    twice in a row, like `xx`, `abcdde` (`dd`), or `aabbccdd` (`aa`, `bb`, `cc`, or `dd`).
    """
    last_ch = None
    for ch in s:
        if ch == last_ch:
            return True
        else:
            last_ch = ch


def check_word(s):
    """
    Returns True if the word is nice by the rules for part 1.
    """
    if contains_naughty_chars(s):
        return False
    if count_vowels(s) < 3:
        return False
    return has_letter_sequence(s)


def check_word_2(s):
    """
    Returns True if the word is nice by the rules for part 2.
    """
    return has_non_overlapping_pairs(s) and has_mirror_letters(s)


def main():
    count = 0
    count_2 = 0
    with open("input.txt", "r") as fin:
        for line in fin:
            if check_word(line):
                count += 1
            if check_word_2(line):
                count_2 += 1

    print("Answer part one: ", count)
    print("Answer part two: ", count_2)


if __name__ == "__main__":
    main()
