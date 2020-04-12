#!/usr/bin/env python3

def split_patterns(P):
    N = len(P)
    preffixes = [""] * N
    suffixes = [""] * N
    all_middle_parts = ""
    for i, p in enumerate(P):
        l = p.split("*")
        preffixes[i] = l[0]
        suffixes[i] = l[len(l) - 1]
        if len(l) > 2:
            all_middle_parts += "".join(l[1:-1])

    return preffixes, suffixes, all_middle_parts


def solve(P):
    preffixes, suffixes, middle = split_patterns(P)

    preffixes.sort(key = lambda s: len(s))
    cur_p = ""
    for p in preffixes:
        if p.startswith(cur_p):
            cur_p = p
        else:
            return "*"

    suffixes.sort(key = lambda s: len(s))
    cur_s = ""
    for s in suffixes:
        if s.endswith(cur_s):
            cur_s = s
        else:
            return "*"

    return cur_p + middle + cur_s


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        P = [None] * N
        for i in range(N):
            P[i] = input().strip()

        result = solve(P)
        print("Case #{}: {}".format(t, result))
