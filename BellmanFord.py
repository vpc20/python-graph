import sys
from collections import deque

from Graph import Digraph


# Bellman-Ford single-source shortest path
def bellman_ford(g, src):
    dist = {}  # distances
    pred = {}  # predecessors
    for u in g.vertices:
        dist[u] = sys.maxsize
        pred[u] = None
    dist[src] = 0

    for _ in range(len(g.vertices) - 1):
        for u, v in g.edges:
            if dist[u] + g.weight(u, v) < dist[v]:  # relaxation
                dist[v] = dist[u] + g.weight(u, v)
                pred[v] = u

    for u, v in g.edges:  # check for negative-weight cycles
        if dist[u] + g.weight(u, v) < dist[v]:
            raise ValueError('Negative-weight cycle detected')

    return pred, dist


# # Bellman-Ford single-source shortest path
# def bellman_ford_sssp(g, source):
#     all_sp = []
#     dist = {}  # distances
#     pred = {}  # predecessors
#     for v in g.vertices:
#         dist[v] = sys.maxsize
#         pred[v] = None
#     dist[source] = 0
#
#     for _ in range(len(g.vertices) - 1):
#         for v1, v2 in g.edges:
#             if dist[v1] + g.weight(v1, v2) < dist[v2]:  # relaxation
#                 dist[v2] = dist[v1] + g.weight(v1, v2)
#                 pred[v2] = v1
#
#     for v1, v2 in g.edges:  # check for negative-weight cycles
#         if dist[v1] + g.weight(v1, v2) < dist[v2]:
#             raise ValueError('Negative-weight cycle detected')
#
#     for v in g.vertices:  # generate all shortest paths
#         if v == source:
#             continue
#         sp = deque(v)  # shortest path
#         curr = v
#         while pred[curr] != source:
#             if pred[curr] not in sp:  # cycle check
#                 sp.appendleft(pred[curr])
#                 curr = pred[curr]
#             else:
#                 print(f'No path to {v}')
#                 break  # cycles are ignored
#         else:
#             sp.appendleft(source)
#             all_sp.append(list(sp))
#
#     return all_sp


if __name__ == '__main__':
    dg = Digraph()  # clrs example
    dg.add_weighted_edges_from([('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4), ('x', 't', -2),
                                ('y', 'x', -3), ('y', 'z', 9), ('z', 'x', 7), ('z', 's', 2),
                                ('s', 't', 6), ('s', 'y', 7)])
    print(f'Graph: {dg}')
    print(f'Weights: {dg.weights}')
    print(bellman_ford(dg, 's'))
    print('')

    # dg = Digraph()
    # dg.add_edge('s', 'a', 3)  # cormen book example
    # dg.add_edge('s', 'c', 5)
    # dg.add_edge('s', 'e', 2)
    # dg.add_edge('a', 'b', -4)
    # dg.add_edge('b', 'g', 4)
    # dg.add_edge('c', 'd', 6)
    # dg.add_edge('d', 'c', -3)
    # dg.add_edge('d', 'g', 8)
    # dg.add_edge('e', 'f', 3)
    # dg.add_edge('f', 'e', -6)
    # dg.add_edge('f', 'g', 7)
    # dg.add_edge('h', 'i', 2)
    # dg.add_edge('i', 'j', 3)
    # dg.add_edge('j', 'h', -8)
    # print(f'Graph: {dg}')
    # print(f'Weights: {dict(dg.weights)}')
    # print(bellman_ford_sssp(dg, 's'))
