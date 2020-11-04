from dimacs import loadDirectedWeightedGraph
from collections import deque
import math
 
(V,L) = loadDirectedWeightedGraph("graphs_test/flow/clique100")

def BFS(graph, source, target, V, parent):
  visited = [False] * V
  queue = []
  queue.append(source)
  visited[source] = True
  while queue:
    u = queue.pop(0)
    for (v,c) in graph[u]:
      if not visited[v] and f_map[(u,v)] > 0:
        queue.append(v)
        visited[v] = True
        parent[v] = u
  return visited[target] #path from s to t exist
def Ford_Fulkerson(graph, source, target, V):
  parent = [-1] * V
  max_flow = 0
  while BFS(graph, 0, V-1, V, parent):
    flow = math.inf
    v = target
    while v != source:
      flow = min(flow, f_map[(parent[v],v)])
      v = parent[v]
    max_flow += flow
    v = target
    while v != source:
      f_map[(parent[v], v)] -= flow
      f_map[(v, parent[v])] += flow
      v = parent[v]
  return max_flow


#adjacency list
graph = [[] for _ in range(V)]
for (x,y,c) in L:
  graph[x-1].append((y - 1,c))
for (x,y,c) in L:
  if (x-1, c) not in graph[y-1]:
    graph[y-1].append((x-1,0))
f_map = {}
for u in range(V):
  for (v,c) in graph[u]:
    f_map[(u,v)] = c
print(Ford_Fulkerson(graph, 0, V-1, V))
