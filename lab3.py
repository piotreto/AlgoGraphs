# https://faliszew.github.io/algograf/lab3
# Piotrek Stecyk

from dimacs import loadWeightedGraph, readSolution
from queue import PriorityQueue
import math
import time


name = "graphs_test/connectivity/grid100x100"

(V, L) = loadWeightedGraph(name)


class Node:
    def __init__(self):
        self.edges = {}
        self.activated = True
        self.merged = []

    def addEdge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight  # dodaj krawędź do zadanego

    def delEdge(self, to):
        del self.edges[to]

    def addMerged(self, v):
        self.merged.append(v)

    def deactivate(self):
        self.activated = False

    def activate(self):
        self.activate = True


def printEdges(G, V):
    for u in range(1, V + 1):
        for (v, c) in G[u].edges.items():
            print("Krawedz miedzy", u, " i ", v, " o wadze ", c)


def mergeVertices(G, x, y):
    if (y in G[x].edges.keys()):
        G[x].delEdge(y)
        G[y].delEdge(x)
    for (v, c) in G[y].edges.items():
        G[v].delEdge(y)
        G[x].addEdge(v, c)
        G[v].addEdge(x, c)
    G[y].edges = {}

def minimumCutPhase(G, wanted):
    visited = [False for _ in range(len(G))]
    distance = [0 for _ in range(len(G))]
    a = 1
    inS = 0
    prev, last = None, None
    Q = PriorityQueue()
    Q.put((-distance[a], a))
    while (inS < wanted):
        v = Q.get()[1]
        if not visited[v]:
            inS += 1
            prev = last
            last = v
            visited[v] = True
            for (u, c) in G[v].edges.items():
                if not visited[u]:
                    distance[u] += c
                    Q.put((-distance[u], u))

    result = distance[last]

    mergeVertices(G, last, prev)

    return result


def minimumCut(G):
    vertices = len(G) - 1
    min = math.inf
    while (vertices > 1):
        result = minimumCutPhase(G, vertices)
        if result < min:
            min = result
        vertices -= 1;
    return min


G = [Node() for i in range(V + 1)]

for (x, y, c) in L:
    G[x].addEdge(y, c)
    G[y].addEdge(x, c)

start_time = time.time()
print(str(minimumCut(G)) == readSolution(name))
print("--- %s seconds ---" % (time.time() - start_time))
