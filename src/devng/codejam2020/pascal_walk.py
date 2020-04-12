#!/usr/bin/env python3

pascal_cache = {}


def pascal(r, k):
    if r < 1 or k < 1 or k > r:
        return 0

    if r == 1 or k  == 1 or r == k:
        return 1

    if (r, k) in pascal_cache:
        return pascal_cache[(r, k)]

    val = pascal(r - 1, k - 1) + pascal(r - 1, k)
    pascal_cache[(r, k)] = val
    return val


def check_pascal_path(path, N):
    if len(path) >  500:
        return False
    s = 1
    for i in range(1, len(path)):
        r, k = path[i - 1]
        p = path[i]
        if p not in ((r - 1, k - 1), (r - 1, k), (r, k - 1), (r, k + 1), (r + 1, k), (r + 1, k + 1)):
            return False
        s += pascal(p[0], p[1])

    return s == N


def print_pascal_triangle():
    for row in range(10):
        print('{: ^45}'.format(' '.join(str(pascal(row, col)) for col in range(row+1))))


def solve1000(N):
    if N > 1000:
        return 0, 0

    path = [(1, 1)]
    if N == 1:
        return path

    final_sum = 1
     # in pascal triangle the diagonal (2,2), (3,2) ... (n, 2) contains
     # sequence of all the natural numbers starting from 1
    r = 2
    while True:
        val = r - 1
        if final_sum + val <= N:
            final_sum += val
            path.append((r, 2))
        else:
            break
        r += 1

    r -= 1
    while final_sum < N:
        path.append((r, 1))
        r +=1
        final_sum += 1

    assert check_pascal_path(path, N)
    return path


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        print("Case #{}:".format(t))
        for r, k in solve1000(N):
            print("{} {}".format(r, k))
