#!/usr/bin/env python3

from collections import deque


class Node:
    def __init__(self, x, y, path):
        self.x = x
        self.y = y
        self.path = path


    def asTuple(self):
        return self.x, self.y


    def __hash__(self):
        return hash((self.x, self.y))


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return "<Node x={} y={} path={}>".format(self.x, self.y, self.path)



def bfs(goal_x, goal_y):
    # we will search for the solution backwards starting from the goal
    goal = Node(goal_x, goal_y, "")
    Q = deque()
    Q.append(goal)
    while Q:
        #print(Q)
        v = Q.popleft()
        x, y = v.asTuple()
        if x == 0 and y == 0:
            return v

        # We came from North
        if x % 2 == 0 and (y - 1) % 2 == 0:
            n = Node(x // 2, (y - 1) // 2, v.path + "N")
            Q.append(n)
        # We came from South
        if x % 2 == 0 and (y + 1) % 2 == 0:
            n = Node(x // 2, (y + 1) // 2, v.path + "S")
            Q.append(n)
         # We came from East
        if (x - 1) % 2 == 0 and y % 2 == 0:
            n = Node((x - 1) // 2, y // 2, v.path + "E")
            Q.append(n)
         # We came from West
        if (x + 1) % 2 == 0 and y % 2 == 0:
            n = Node((x + 1) // 2, y // 2, v.path + "W")
            Q.append(n)

    return None


def solve(X, Y):
    node = bfs(X, Y)
    if node:
        return node.path

    return "IMPOSSIBLE"


if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    T = int(input())
    for t in range(1, T + 1):
        X, Y = list(map(int, input().split()))
        result = solve(X, Y)
        print("Case #{}: {}".format(t, result))
