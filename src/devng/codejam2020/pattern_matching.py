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
    result = [""] * 10000
    N = len(P)
    p, s, middle = split_patterns(P)

    for i in range(N):
        p_i = p[i]
        s_i = s[i]
        for i in range(len(p_i)):
            p_ch = p_i[i]
            r_ch = result[i]
            if r_ch == "":
                result[i] = p_ch
            elif r_ch != p_ch:
                return "*"

        for i in range(len(s_i)):
            s_ch = s_i[len(s_i) - 1 - i]
            r_i = len(result) - 1 - i
            r_ch = result[r_i]
            if r_ch == "":
                result[r_i] = s_ch
            elif r_ch != s_ch:
                return "*"

    # add all middle parts and join the result array into a string
    result[result.index("")] = middle
    return "".join(result)


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        P = [None] * N
        for i in range(N):
            P[i] = input().strip()

        result = solve(P)
        print("Case #{}: {}".format(t, result))
