#!/usr/bin/env python3
# coding: utf-8


class Dancer:
    def __init__(self, x, y, skill):
        self.x = x
        self.y = y
        self.skill = skill
        self.prio = skill
        self.deleted = False
        self.hashval = hash((x, y))
        self.compass_neighbors = set()


    def addCompassNeighbor(self, neighbor):
        if ((neighbor.x == self.x or neighbor.y == self.y)
                and neighbor not in self.compass_neighbors
                and neighbor != self):
            self.compass_neighbors.add(neighbor)


    def removeCompassNeighbor(self, neighbor):
        if neighbor in self.compass_neighbors:
            self.compass_neighbors.remove(neighbor)


    def removeItselfFromNeighbors(self):
        self.deleted = True
        self.skill = 0
        n_x = None
        n_y = None
        for cn in self.compass_neighbors:
            cn.removeCompassNeighbor(self)
            if cn.deleted:
                continue
            if cn.x == self.x:
                if n_x:
                    cn.addCompassNeighbor(n_x)
                    n_x.addCompassNeighbor(cn)
                else:
                    n_x = cn
            if cn.y == self.y:
                if n_y:
                    cn.addCompassNeighbor(n_y)
                    n_y.addCompassNeighbor(cn)
                else:
                    n_y = cn
        result = self.compass_neighbors
        self.compass_neighbors = set()
        return result


    def computePrio(self):
        if len(self.compass_neighbors) > 0:
            self.prio = self.skill - sum([cn.skill for cn in self.compass_neighbors]) / len(self.compass_neighbors)
        else:
            self.prio = self.skill


    # required by heapq for sorting
    def __lt__(self, other):
        return self.prio < other.prio


    def __hash__(self):
        return self.hashval


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return "<Dancer x={} y={} skill={} prio={} deleted={}>".format(self.x, self.y, self.skill, self.prio, self.deleted)



def solve(R, C, dance_floor):
    # Create dancer graph from input array
    dancer_graph = []
    for y in range(R):
        for x in range(C):
            d = Dancer(x, y, dance_floor[y][x])
            dancer_graph.append(d)

    # Initially all dancers have adjacent compass neighbors
    for d in dancer_graph:
        if d.x - 1 >= 0:
            d.addCompassNeighbor(dancer_graph[d.y * C + d.x - 1])
        if d.y - 1 >= 0:
            d.addCompassNeighbor(dancer_graph[(d.y -1) * C + d.x])
        if d.x + 1 < C:
            d.addCompassNeighbor(dancer_graph[d.y * C + d.x + 1])
        if d.y + 1 < R:
            d.addCompassNeighbor(dancer_graph[(d.y + 1) * C + d.x])

    interest_level_round = 0
    to_be_removed = set()
    for d in dancer_graph:
        d.computePrio()
        interest_level_round += d.skill
        if d.prio < 0:
            to_be_removed.add(d)

    interest_level_competition = interest_level_round
    affected_nodes = set()
    while True:
        interest_level_drop = 0
        affected_nodes.clear()
        for d in to_be_removed:
            interest_level_drop += d.skill
            affected_nodes.update(d.removeItselfFromNeighbors())

        if len(affected_nodes) == 0:
            break

        to_be_removed.clear()
        interest_level_round -= interest_level_drop
        interest_level_competition += interest_level_round
        for a in affected_nodes:
            a.computePrio()
            if a.prio < 0:
                to_be_removed.add(a)

    return interest_level_competition


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        R, C = list(map(int, input().split()))
        dance_floor = []
        for _ in range(R):
            dance_floor.append(list(map(int, input().split())))

        interest_level = solve(R, C, dance_floor)
        print("Case #{}: {}".format(t, interest_level))
