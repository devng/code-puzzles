#!/usr/bin/env python3

from copy import deepcopy

DEBUG = False

pascal_cache = {}


# get value for position r, k in the pascal triangle
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
        print("path too large", len(path))
        return False
    visited = set((1, 1))
    s = 1
    for i in range(1, len(path)):
        r, k = path[i - 1]
        p = path[i]
        if p in visited:
            print("already visited", p[0], p[1], path)
            return False
        visited.add(p)
        if p not in ((r - 1, k - 1), (r - 1, k), (r, k - 1), (r, k + 1), (r + 1, k), (r + 1, k + 1)):
            print("not a neighbor", r, k, path)
            return False
        s += pascal(p[0], p[1])

    if s != N:
        print(path)
        print ("Sum is not equal to N", s, N)
        return False
    return True


# For fun print pascal triangle of size 10 to the console
def print_pascal_triangle(N=10):
    for row in range(N):
        print('{: ^45}'.format(' '.join(str(pascal(row, col)) for col in range(row+1))))


def solveSmallN(N, path=[(1, 1)], r=2, flip_row=False, sum_so_far=1):
    if N <= 0:
        return []
    if N == 1:
        return [(1, 1)]

    # in python default values are assigned only the first time
    # thus if the value is not immutable one would have a problem the second
    # time the function is invoked
    path = deepcopy(path)

    # in pascal triangle the diagonal (2,2), (3,2) ... (n, 2) contains
    # sequence of all the natural numbers starting from 1
    while sum_so_far + r - 1 <= N:
        k = r - 1 if flip_row else 2
        sum_so_far += r - 1
        path.append((r, k))
        r += 1

    r -= 1
    while sum_so_far < N:
        k = r if flip_row else 1
        if (r, k) not in path:
            path.append((r, k))
            sum_so_far += 1
        r +=1

    if DEBUG:
        assert check_pascal_path(path, N)
    return path


def solve(N):
    if N < 31:
        return solveSmallN(N)

    #We need N - 30 because 10^9 requires max 30 bits and we need to connect the rows with a path
    n_left = N - 30

    # the the sum of a row in pascal triangle equal sum(row) = 2^(row-1)
    # get the number bits and create a path out of those
    bitfield = list(bin(n_left))[2:]
    sum_so_far = 0
    flip_row = False
    path = []
    max_row = 0
    for i, b in enumerate(reversed(bitfield)):
        full_row = b == '1'
        r = i + 1
        if full_row:
            for k in range(1, r + 1):
                k = r + 1 - k if flip_row else k
                path.append((r, k))
            sum_so_far += 2**i
            flip_row = not flip_row
            max_row = r
        else:
            # if the bit is 0 we append just the most left or right 1
            # in the triangle row which always has the value 1
            k = r if flip_row else 1
            path.append((r, k))
            sum_so_far += 1

    # fill the rest by running along side the diagonals
    if sum_so_far < N:
        path = solveSmallN(N, path, max_row + 1, flip_row, sum_so_far)

    if DEBUG:
        assert check_pascal_path(path, N)
    return path

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        print("Case #{}:".format(t))
        for r, k in solve(N):
            print("{} {}".format(r, k))
