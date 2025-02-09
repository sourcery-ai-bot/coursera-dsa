#!/usr/bin/python3


import sys
import queue


# Maximum allowed edge length
maxlen = 2 * 10**6


class DistPreprocessLarge:
    def __init__(self, n, adj, cost):
        # See description of these parameters in the starter for
        # friend_suggestion
        self.n = n
        self.INFINITY = n * maxlen
        self.adj = adj
        self.cost = cost
        self.bidistance = [[self.INFINITY] * n, [self.INFINITY] * n]
        self.visited = [False] * n
        self.visited = []
        self.q = queue.PriorityQueue()
        # Levels of nodes for node ordering heuristics
        self.level = [0] * n
        # Positions of nodes in the node ordering
        self.rank = [0] * n

    def mark_visited(self, x):
        if not self.visited[x]:
            self.visited[x] = True
            self.visited.append(x)

    def add_arc(self, u, v, c):
        def update(adj, cost, u, v, c):
            for i in range(len(adj[u])):
                if adj[u][i] == v:
                    cost[u][i] = min(cost[u][i], c)
                    return
            adj[u].append(v)
            cost[u].append(c)

        update(self.adj[0], self.cost[0], u, v, c)
        update(self.adj[1], self.cost[1], v, u, c)

    # Makes shortcuts for contracting node v
    def shortcut(self, v):
        # Implement this method yourself

        # Compute the node importance in the end
        shortcut_count = 0
        neighbors = 0
        shortcut_cover = 0
        level = 0
        # Compute correctly the values for the above heuristics before
        # computing the node importance
        importance = (shortcut_count - len(self.adj[0][v]) - len(
            self.adj[1][v])) + neighbors + shortcut_cover + level
        return importance, shortcuts, level

    # See description of this method in the starter for friend_suggestion
    def clear(self):
        for v in self.visited:
            self.bidistance[0][v] = self.bidistance[1][v] = self.INFINITY
            self.visited[v] = False
        del self.visited[:]

    # See description of this method in the starter for friend_suggestion
    def visit(self, side, v, dist):
        # Implement this method yourself
        pass

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        estimate = self.INFINITY
        self.visit(0, s, 0)
        self.visit(1, t, 0)
        # Implement the rest of the algorithm yourself

        return -1 if estimate == self.INFINITY else estimate


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for _ in range(m):
        u, v, c = readl()
        adj[0][u - 1].append(v - 1)
        cost[0][u - 1].append(c)
        adj[1][v - 1].append(u - 1)
        cost[1][v - 1].append(c)

    ch = DistPreprocessLarge(n, adj, cost)
    print("Ready")
    sys.stdout.flush()
    t, = readl()
    for _ in range(t):
        s, t = readl()
        print(ch.query(s - 1, t - 1))
