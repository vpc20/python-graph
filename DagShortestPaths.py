import sys

from Graph import Digraph
from TopologicalSort import topological_sort


# dag single-source shortest paths
def dag_sssp(g, src):
    sortedv = topological_sort(g)

    dist = {}  # distances
    pred = {}  # predecessors
    for v in g.vertices:
        dist[v] = sys.maxsize
        pred[v] = None
    dist[src] = 0

    for u in sortedv:
        for v in g.neighbors(u):
            if dist[u] + g.weight(u, v) < dist[v]:  # relaxation
                dist[v] = dist[u] + g.weight(u, v)
                pred[v] = u

    return pred, dist


# def dag_sssp(g, source):
#     all_sp = []
#     sortedv = topological_sort(g)
#
#     dist = {}  # distances
#     pred = {}  # predecessors
#     for v in g.vertices():
#         dist[v] = sys.maxsize
#         pred[v] = None
#     dist[source] = 0
#
#     for v1 in sortedv:
#         for v2 in g.neighbors(v1):
#             if dist[v1] + g.weight(v1, v2) < dist[v2]:  # relaxation
#                 dist[v2] = dist[v1] + g.weight(v1, v2)
#                 pred[v2] = v1
#
#     for v in g.vertices():  # generate all shortest paths
#         if v == source or pred[v] is None:
#             continue
#         sp = deque(v)  # shortest path
#         curr = v
#         while pred[curr] != source:
#             sp.appendleft(pred[curr])
#             curr = pred[curr]
#         sp.appendleft(source)
#         all_sp.append(list(sp))
#
#     return all_sp


if __name__ == '__main__':
    dg = Digraph()  # clrs example
    dg.add_weighted_edges_from([('r', 's', 5), ('r', 't', 3), ('s', 't', 2), ('s', 'x', 6),
                                ('t', 'x', 7), ('t', 'y', 4), ('t', 'z', 2), ('x', 'y', -1),
                                ('x', 'z', 1), ('y', 'z', -2)])
    print(dag_sssp(dg, 's'))
