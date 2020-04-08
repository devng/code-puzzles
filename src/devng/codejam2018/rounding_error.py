#!/usr/bin/env python3

DEBUG = False

import heapq


# calculates a percent for a given integer i and max N
# it also returns the priority for the queue
def percent(i, N):
    p = (i / N) * 100
    p_int = int(p)
    delta = p - p_int
    if (delta >= 0.5):
        return p_int + 1, 100
    else:
        return p_int, 0.5 - delta


def solve(C, N):
    votes_left = N - sum(C)
    C.extend([0] * votes_left)

    # Keep a priority queue on what we need to do next
    pq = [(percent(c, N)[1], i) for i, c in enumerate(C)]
    heapq.heapify(pq)

    for _ in range(votes_left):
        _, i = heapq.heappop(pq)
        C[i] += 1
        heapq.heappush(pq, (percent(C[i], N)[1], i))

    result = 0
    for c in C:
        result += percent(c, N)[0]
    return result


if DEBUG:
    print(solve([1, 1], 3))
    print("--------------------------")
    print(solve([1, 3, 2], 10))
    print("--------------------------")
    print(solve([3, 1], 6))
    print("--------------------------")
    print(solve([1, 1, 1, 1, 1, 1, 1, 1], 9))
    print("--------------------------")


if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    num_cases = int(input())
    for i in range(1, num_cases + 1):
        N, L = list(map(int, input().split()))
        C = list(map(int, input().split()))
        result = solve(C, N)
        print("Case #{}: {}".format(i, result))
