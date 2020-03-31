import sys
from collections import deque

from Graph import Digraph
from TopologicalSort import topological_sort_dfs


# dag single-source shortest paths
def dag_sssp(g, source):
    all_sp = []
    sorted_v = topological_sort_dfs(g)

    dist = {}  # distances
    pred = {}  # predecessors
    for v in g.vertices():
        dist[v] = sys.maxsize
        pred[v] = None
    dist[source] = 0

    for v1 in sorted_v:
        for v2 in g.neighbors(v1):
            if dist[v1] + g.get_weight(v1, v2) < dist[v2]:  # relaxation
                dist[v2] = dist[v1] + g.get_weight(v1, v2)
                pred[v2] = v1

    for v in g.vertices():  # generate all shortest paths
        if v == source or pred[v] is None:
            continue
        sp = deque(v)  # shortest path
        curr = v
        while pred[curr] != source:
            sp.appendleft(pred[curr])
            curr = pred[curr]
        sp.appendleft(source)
        all_sp.append(list(sp))

    return all_sp


if __name__ == '__main__':
    dg = Digraph()
    dg.add_edge('r', 's', 5)
    dg.add_edge('r', 't', 3)
    dg.add_edge('s', 't', 2)
    dg.add_edge('s', 'x', 6)
    dg.add_edge('t', 'x', 7)
    dg.add_edge('t', 'y', 4)
    dg.add_edge('t', 'z', 2)
    dg.add_edge('x', 'y', -1)
    dg.add_edge('x', 'z', 1)
    dg.add_edge('y', 'z', -2)
    print(dag_sssp(dg, 's'))