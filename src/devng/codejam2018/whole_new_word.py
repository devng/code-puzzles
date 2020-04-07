#!/usr/bin/env python3

from itertools import product


def find_word(words, n, l):
    words_set = set(words)
    chars = []
    # put all characters in sets per columns
    for i in range(l):
        chars.append({w[i] for w in words})
    # print(chars)

    """
    # generates all word prefixes
    prefs = []
    for n in range(l):
        prefs.append({w[:n+1] for w in words})
    print(prefs)
    """

    # because Vincetn can provide only up to 2000 words, need to check not more than 2001 words
    # to see if we can make a word or not, thus checkking all possibilities is feasible in this case.
    # Note: that product() is a python generator so we don't generate all possibilities up front
    # but only one at a time on each loop step.
    for p in product(*chars):
        w = "".join(p)
        if w not in words_set:
            return w
    return "-"


if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    num_cases = int(input())
    for i in range(1, num_cases + 1):
        n, l = list(map(int, input().split()))
        words = []
        for _ in range(n):
            words.append(input())
        result = find_word(words, n, l)
        print("Case #{}: {}".format(i, result))
