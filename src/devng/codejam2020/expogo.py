#!/usr/bin/env python3

from collections import deque
from collections import namedtuple

Node = namedtuple("Node", ["x", "y", "path"])


def bfs(goal_x, goal_y):
    # we will search for the solution backwards starting from the goal
    Q = deque()
    Q.append(Node(goal_x, goal_y, ""))
    while Q:
        # print(Q)
        x, y, path = Q.popleft()
        if x == 0 and y == 0:
            return path
        # We came from North
        if x % 2 == 0 and (y - 1) % 2 == 0:
            Q.append(Node(x // 2, (y - 1) // 2, path + "N"))
        # We came from South
        if x % 2 == 0 and (y + 1) % 2 == 0:
            Q.append(Node(x // 2, (y + 1) // 2, path + "S"))
        # We came from East
        if (x - 1) % 2 == 0 and y % 2 == 0:
            Q.append(Node((x - 1) // 2, y // 2, path + "E"))
        # We came from West
        if (x + 1) % 2 == 0 and y % 2 == 0:
            Q.append(Node((x + 1) // 2, y // 2, path + "W"))
    return "IMPOSSIBLE"


if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    T = int(input())
    for t in range(1, T + 1):
        X, Y = list(map(int, input().split()))
        result = bfs(X, Y)
        print("Case #{}: {}".format(t, result))
