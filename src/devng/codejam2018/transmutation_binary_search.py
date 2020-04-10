#!/usr/bin/env python3

# This solution only passes all 3 test sets
# Run time complexity is O(M^3 log S)

DEBUG = False

def solve(M, R, G):

    def can_produce(r, target_g, g_left, seen):
        if r in seen:
            return False

        i = r - 1 # index starts from 0, but r starts from 1
        left = g_left[i] - target_g

        if left >= 0:
            g_left[i] = left
            return True
        else:
            g_left[i] = 0

        seen.add(r)
        r1, r2 = R[r]
        next_target = -left
        if (can_produce(r1, next_target, g_left, seen.copy())):
            return can_produce(r2, next_target, g_left, seen.copy())
        return False

    # do binary search for the max possible production
    target_high = sum(G) + 1 # impossible to reach amount
    target_low = 0
    result = 0
    while target_high - target_low > 1:
        target_next = (target_high + target_low) // 2
        success = can_produce(1, target_next, G.copy(), set())
        if success:
            result = max(result, target_next)
            target_low = target_next
        else:
            target_high = target_next

    return result


def can_produce(R, r, target_g, seen, g_left):
    if r in seen:
        return False

    i = r - 1
    left = g_left[i] - target_g
    g_left[i] = left

    if left >= 0:
        return True

    next_seen = seen.copy()
    next_seen.add(r)

    r1, r2 = R[r]
    target_g_r1 = -left
    target_g_r2 = -left
    if (can_produce(R, r1, target_g_r1, next_seen, g_left)):
        return can_produce(R, r2, target_g_r2, next_seen, g_left)
    return False


if DEBUG:
    print("----------------------------")
    print(solve(3, {1: [2, 3], 2: [1, 3], 3: [1, 2]}, [5, 2, 3]))
    print("----------------------------")
    print(solve(4, {1: [2, 3], 2: [3, 4], 3: [2, 4], 4: [2, 3]}, [5, 2, 3, 2]))
    print("----------------------------")
    print(solve(5, {1: [3, 4], 2: [3, 4], 3: [4, 5], 4: [3, 5], 5: [1, 3]}, [0, 8, 6, 2, 4]))
    print("----------------------------")
    print(solve(4, {1: [3, 4], 2: [2, 3], 3: [2, 3], 4: [2, 3]}, [0, 1, 1, 0]))
    print("----------------------------")
    print(solve(4, {1: [3, 4], 2: [2, 3], 3: [2, 3], 4: [2, 3]}, [0, 0, 0, 0]))



if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    T = int(input())
    for i in range(1, T + 1):
        M = int(input())
        R = {}
        for r in range(1, M + 1):
            R[r] = list(map(int, input().split()))

        G = list(map(int, input().split()))
        result = solve(M, R, G)
        print("Case #{}: {}".format(i, result))
