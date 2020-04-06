#!/usr/bin/env python3
# coding: utf-8

from itertools import product
from copy import deepcopy

SLOW_CASE_CACHE = {
    (5, 6):  ["IMPOSSIBLE", None],
    (5, 11): ["POSSIBLE",
           [[2, 1, 3, 4, 5],
            [1, 2, 4, 5, 3],
            [4, 5, 2, 3, 1],
            [3, 4, 5, 1, 2],
            [5, 3, 1, 2, 4]]],
    (5, 19): ["POSSIBLE",
           [[4, 1, 2, 5, 3],
            [2, 4, 5, 3, 1],
            [3, 5, 4, 1, 2],
            [5, 3, 1, 2, 4],
            [1, 2, 3, 4, 5]]],
    (5, 24): ["IMPOSSIBLE", None],
}

def gen_sum_arr(n, target_sum):
    """
    Generates an array for the trace of the latin square of size N with a given target sum.
    Returns all possible traces as arrays that sum up to the target_sum.
    """
    result = []
    for p in product([x + 1 for x in range(n)], repeat=n):
        if sum(p) == target_sum:
            result.append(p)
    if result:
        # only return half of the result + 1, since the others are the same just mirrored
        return result[:(len(result) + 1)//2]
    return result


def gen_matrix(n, k):
    """
    Generates and returns a matrix of size NxN with a trace with sum equals to K,
    all other fields are 0. If no such matrix can be generated empty array is returned.
    """
    diagonals = gen_sum_arr(n, k)

    result = []
    if not diagonals:
        return result

    for d in diagonals:
        m = [[0] * n for i in range(n)]
        for i in range(n):
            m[i][i] = d[i]
        result.append(m)
    return result


def is_latin_sq(m):
    """
    Check if the provided matrix m is a latin square
    Returns:
        * 1 if the matrix is a latin square and they are no empty fields (i.e, fields with value of 0)
        * 0 if the matrix is a latin square (thus far) but there are still fields with value 0
        * -1 if the matrix is definitely no latin square
    """
    not_full = False
    for i in range(len(m)):
        cur_num_row = {}
        cur_num_col = {}
        for j in range(len(m[i])):
            # we can check both rows and columns at the same time
            # since this is an NxN matrix
            num_row = m[i][j]
            num_col = m[j][i]

            if num_row != 0:
                if num_row not in cur_num_row:
                    cur_num_row[num_row] = True
                else:
                    return -1
            else:
                not_full = True

            if num_col != 0:
                if num_col not in cur_num_col:
                    cur_num_col[num_col] = True
                else:
                    return -1
            else:
                not_full = True

    if not_full:
        return 0
    else:
        return 1


def find_matrix(n, k, use_cache=True):
    """
    Tries to find a matrix of size NxN which satisfies the two criteria:
    * trace sums up to K
    * the matrix is a latin square
    Returns a tuple of 2 elements. First element is the string 'POSSIBLE' or 'IMPOSSIBLE'.
    In the case of 'POSSIBLE' we also return a single example matrix.
    """
    if use_cache and (n, k) in SLOW_CASE_CACHE:
        return SLOW_CASE_CACHE[(n, k)]

    # Speed up the search process by assigning possible NxN matrices with trace with sum K
    solution_stack = gen_matrix(n, k)

    while len(solution_stack) > 0:
        m = solution_stack.pop()

        for i in range(n):
            for j in range(n):
                if m[i][j] == 0:
                    # empty cell try to fill it with values and put it on the stack
                    for val in range(n, 0, -1):
                        m[i][j] = val
                        latin_score = is_latin_sq(m)
                        if latin_score == 0:
                            solution_stack.append(deepcopy(m))
                        elif latin_score == 1:
                            return "POSSIBLE", m

    return "IMPOSSIBLE", None


if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most Code Jam problems.
    num_cases = int(input()) # read a line with a single integer
    for i in range(1, num_cases + 1):
        line = input()
        n = list(map(int, line.split()))
        result = find_matrix(n[0], n[1])
        print("Case #{}: {}".format(i, result[0]))
        if result[0] == "POSSIBLE":
            for row in result[1]:
                print(*row)
