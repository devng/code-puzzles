#!/usr/bin/env python3

# This solution only passes the first two test sets
# Run time complexity is O(M*S)

DEBUG = False

def solve(M, R, G):
    # print(M, R, G)

    G.insert(0, 0) # make the indexes work without convertion
    def next_metal(r, visited):
        if r not in R:
            visited.add(r)
            return False

        r1, r2 = R[r]
        if r1 == 1 or r2 == 1:
            return False

        if G[r1] > 0 and G[r2] > 0:
            G[r] += 1
            G[r1] -= 1
            G[r2] -= 1
            visited.add(r)
            return True
        elif G[r1] == 0 and r1 not in visited:
            visited.add(r)
            return next_metal(r1, visited)
        elif G[r2] == 0 and r2 not in visited:
            visited.add(r)
            return next_metal(r2, visited)
        else:
            visited.add(r)
            return False

    while next_metal(1, set([1])):
        pass

    return G[1]


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
