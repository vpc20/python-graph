import sys
from collections import deque
from heapq import heappop, heappush

from Graph import Digraph


# Dijkstra single-source shortest path
# def dijkstra_sssp(g, source):
#     all_sp = []
#     visited = set()
#     dist = {}  # distances
#     pred = {}  # predecessors
#     for v in g.vertices():
#         dist[v] = sys.maxsize
#         pred[v] = None
#     dist[source] = 0
#
#     minq = [(0, '', source)]
#     while minq:
#         _, _, v1 = heappop(minq)
#         if v1 in visited:
#             continue
#         for v2 in g.neighbors(v1):
#             if v2 not in visited:
#                 if dist[v1] + g.get_weight(v1, v2) < dist[v2]:  # relaxation
#                     dist[v2] = dist[v1] + g.get_weight(v1, v2)
#                     pred[v2] = v1
#                     heappush(minq, (dist[v2], v1, v2))
#         visited.add(v1)
#
#     for v in g.vertices():  # generate all shortest paths
#         if v == source or pred[v] is None:
#             continue
#         sp = deque([v])  # shortest path
#         curr = v
#         while pred[curr] != source:
#             sp.appendleft(pred[curr])
#             curr = pred[curr]
#         sp.appendleft(source)
#         all_sp.append((dist[v], list(sp)))
#
#     return all_sp


def dijkstra_sssp(g, source):
    all_sp = []
    visited = set()
    dist = {}  # distances
    pred = {}  # predecessors
    for v in g.vertices():
        dist[v] = sys.maxsize
        pred[v] = None
    dist[source] = 0

    minq = [(0, source)]
    while minq:
        _, v1 = heappop(minq)
        if v1 not in visited:
            for v2 in g.neighbors(v1):
                if v2 not in visited:
                    d = dist[v1] + g.get_weight(v1, v2)
                    if d < dist[v2]:  # relaxation
                        dist[v2] = d
                        pred[v2] = v1
                        heappush(minq, (dist[v2], v2))
            visited.add(v1)

    for v in g.vertices():  # generate all shortest paths
        if v == source or pred[v] is None:
            continue
        sp = deque([v])  # shortest path
        curr = v
        while pred[curr] != source:
            sp.appendleft(pred[curr])
            curr = pred[curr]
        sp.appendleft(source)
        all_sp.append((dist[v], list(sp)))

    return all_sp


if __name__ == '__main__':
    dg = Digraph()
    dg.add_edge('s', 't', 10)  # cormen book example
    dg.add_edge('s', 'y', 5)
    dg.add_edge('t', 'x', 1)
    dg.add_edge('t', 'y', 2)
    dg.add_edge('x', 'z', 4)
    dg.add_edge('y', 't', 3)
    dg.add_edge('y', 'x', 9)
    dg.add_edge('y', 'z', 2)
    dg.add_edge('z', 's', 7)
    dg.add_edge('z', 'x', 6)
    print(dg)
    print(dijkstra_sssp(dg, 's'))

    # cp3 4.3 in https://visualgo.net/en/dfsbfs
    dg = Digraph()
    dg.add_edge(0, 1)
    dg.add_edge(0, 4)
    dg.add_edge(1, 2)
    dg.add_edge(1, 5)
    dg.add_edge(2, 3)
    dg.add_edge(2, 6)
    dg.add_edge(3, 7)
    dg.add_edge(4, 8)
    dg.add_edge(5, 6)
    dg.add_edge(5, 10)
    dg.add_edge(6, 11)
    dg.add_edge(7, 12)
    dg.add_edge(8, 9)
    dg.add_edge(9, 10)
    dg.add_edge(10, 11)
    dg.add_edge(11, 12)
    print(dg)
    print(dijkstra_sssp(dg, 0))



