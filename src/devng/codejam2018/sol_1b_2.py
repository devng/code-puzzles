#!/usr/bin/env python3

# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007764/000000000003675b

def get_run(S, start, N, M):
    n = N[start]
    i = start
    while i < S and N[i] == n:
        i += 1
    skip = i - start
    if i == S:
        return skip, i - start
    m = M[i]
    i += 1
    while i < S and (M[i] == m or N[i] == n):
        i += 1
    return skip, i - start


def solve(S, N, M):
    start = 0
    best_run = 0
    count = 0
    next_n = 0
    next_m = 0
    while start < S:
        if S - start < best_run:
            break

        n_run = 0
        if start >= next_n:
            n_skip, n_run = get_run(S, start, N, M)
            next_n = start + n_skip

        # swap the N and M arrays
        m_run = 0
        if start >= next_m:
            m_skip, m_run = get_run(S, start, M, N)
            next_m = start + m_skip

        size = max(n_run, m_run)
        if size > best_run:
            best_run = size
            count = 1
        elif size == best_run:
            count += 1
        start += 1

    return best_run, count


"""
print(solve(5, [9, 9, 18, 22, 22], [-10, -5, 7, -1, -1]))
print("###################################")
print(solve(5, [4, 4, 4, 6, 8], [-2, 0, 2, 2, 2]))
"""

if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    T = int(input())
    for i in range(1, T + 1):
        S = int(input())
        N = [None] * S
        M = [None] * S
        for j in range(S):
            d, a, b = list(map(int, input().split()))
            M[j] = d + a
            N[j] = d - b

        result = solve(S, N, M)
        print("Case #{}: {} {}".format(i, *result))
