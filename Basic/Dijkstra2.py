#!/usr/bin/python
# -*- coding: UTF-8 -*-

# [Dijkstra algorithm](http://jpython.blogspot.com/2015/10/dijkstra-algorithm.html)

from heapq import heappush, heappop

# 0 index base dijkstra algorithm
def Dijkstra(graph, source):
    A = [None] * len(graph)
    queue = [(0, source)]
    while queue:
        path_len, v = heappop(queue)
        # v未遍历，查找v的对应路径
        if A[v] is None: # v is unvisited
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len, w))

    # set -1 for unreachable
    return [-1 if x is None else x for x in A]

graph = {
  0: { 1:2, 2:4, 3:1 },
  1: { 2:1, 3:3 },
  2: { 4: 7},
  3: { 2: 2 },
  4: { 0:2, 3:3 },
  5: {}
}
source = 0

print Dijkstra(graph, source)

