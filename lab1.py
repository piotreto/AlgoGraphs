from dimacs import *
from sys import argv


class Node:
  def __init__(self, id):
    self.id = id
    self.parent = self
    self.rank = 0

def find_set(x):
  if x != x.parent:
    x.parent = find_set(x.parent)
  return x.parent

def union(x, y):
  x = find_set(x)
  y = find_set(y)
  if x.rank > y.rank:
    y.parent = x
  else:
    x.parent = y
    if x.rank == y.rank:
      y.rank += 1

def tourist_guide(s,t, name):
  (n, L) = loadWeightedGraph(name)
  L.sort(key = lambda x: x[2], reverse=True)
  V=[Node(i) for i in range(n+1)]
  for (x,y,w) in L:
    union(V[x],V[y])
    if(find_set(V[s]) == find_set(V[t])):
      return w
print(tourist_guide(1,2,argv[1]))

def DFS( G, s, t):   # DFS w grafie G z wierzchołka s
  V = len(G)            # liczba wierzchołków w grafie (zakładając powyższą implementację)
  visited = [False] * V
  DFSVisit(G, s, visited)
  return visited[t]

def DFSVisit( G, s, min_max, visited): # rekurencyjna funkcja realizująca DFS
  visited[s] = True
  for (v, w) in G[s]:
    if not visited[v] and w >= min_max:
      DFSVisit(G, v, min_max, visited)







