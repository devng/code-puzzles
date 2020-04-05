#!/usr/bin/env python

# Make the script compatible with python 3.x
from __future__ import absolute_import, division, print_function, unicode_literals

START = 97 # a
END = 122  # z
EXCLUDE = "iol"


def increment_string(s):
    result = []
    inc = 1
    for i in range(len(s) -1, -1, -1):
        r = ord(s[i]) + inc
        if r > END:
            r = START
            inc = 1
        elif s[i] in EXCLUDE:
            return s[0:i] + chr(r+1) + ('a'  * (len(s)-i-1))
        else:
            inc = 0
        result.append(chr(r))
    result.reverse()
    return "".join(result)


def is_password_valid(s):
    p1 = 0
    p2 = 0
    has_3_increasing_chars = False
    non_overlapping_pairs = 0
    last_non_overlapping_pair = 0
    for ch in s:
        # the letters i, o, or l are not allowed
        if ch in EXCLUDE:
            return False
        r = ord(ch)
        if p1 + 1 == p2 and p2 + 1 == r:
            has_3_increasing_chars = True
        p1 = p2
        p2 = r
        pair = p1 + p2
        if p1 == p2 and last_non_overlapping_pair != pair:
            non_overlapping_pairs += 1
            last_non_overlapping_pair = pair

    # print(s, has_3_increasing_chars, non_overlapping_pairs, last_non_overlapping_pair)

    return has_3_increasing_chars and non_overlapping_pairs >= 2


def next_valid_password(s):
    s = increment_string(s)
    for i in range(100000000):
        if is_password_valid(s):
            return s
        else:
            s = increment_string(s)
    return None


if __name__ == "__main__":
    p1 = next_valid_password("vzbxkghb")
    p2 = next_valid_password(p1)
    print("Answer part one: %s\nAnswer part two: %s" % (p1, p2))
