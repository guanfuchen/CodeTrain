#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 主要参考[dijkstra.py](https://gist.github.com/kachayev/5990802)

from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    # dij算法中第一步，f->f=0，seen记录连接结点，未连接为inf
    # 其中q存储了距离，达到的结点，和所需的路径
    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            # 如果v1就是终点，返回当前代价和路径
            if v1 == t: return cost, path

            # 获取v1的邻接点
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")

if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    # print edges
    print "A -> E:"
    print dijkstra(edges, "A", "E")
    print "F -> G:"
    print dijkstra(edges, "F", "G")
    print "F -> H:"
    print dijkstra(edges, "F", "H")
