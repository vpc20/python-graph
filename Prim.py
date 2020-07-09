import sys
from heapq import heappush, heappop
from Graph import Graph


def mst_prim(g):
    """
    The minimum spanning tree of a connected, undirected graph is a subgraph of the graph (a tree) with the
    minimum sum of edge weights.

    :param g: input Graph
    :return: minimum spannning tree
    :rtype: Graph
    """
    seen = set()
    min_wt = dict()
    parent = dict()

    for v in g.vertices:
        min_wt[v] = sys.maxsize
        parent[v] = None

    root = g.vertices[0]  # take first vertex as root
    min_wt[root] = 0
    minq = [(0, root)]
    while minq:
        _, u = heappop(minq)
        for v in g.neighbors(u):
            if (u, v) not in seen:
                ewt = g.weight(u, v)
                if ewt < min_wt[v]:
                    parent[v] = u
                    min_wt[v] = ewt
                    heappush(minq, (ewt, v))
                seen.add((u, v))
                seen.add((v, u))
    # create mst
    parent.pop(root)  # remove the root
    mst = Graph()
    for v, u in parent.items():
        mst.add_edge(u, v, g.weight(u, v))
    return mst


if __name__ == '__main__':
    g = Graph()
    g.add_weighted_edges_from([('a', 'b', 4), ('a', 'h', 8), ('b', 'c', 8), ('b', 'h', 11), ('c', 'd', 7),
                               ('c', 'f', 4), ('c', 'i', 2), ('i', 'g', 6), ('i', 'h', 7), ('f', 'd', 14),
                               ('f', 'e', 10), ('f', 'g', 2), ('e', 'd', 9), ('g', 'h', 1)])
    print(mst_prim(g).edges)
