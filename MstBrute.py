# minimum spanning tree
import sys
from itertools import combinations

from Graph import Graph, is_spanning_tree


def mst_brute(g):
    minw = sys.maxsize
    min_edges = []
    edges = g.edges()
    for r in range(1, len(edges) + 1):
        for comb in combinations(edges, r):
            # print(comb)
            g1 = Graph()
            g1.add_edges_from(comb)
            if is_spanning_tree(g, comb):
                wsum = sum([g.weight(v1, v2) for v1, v2 in comb])
                if wsum < minw:
                    minw = wsum
                    min_edges = comb
    return minw, min_edges


if __name__ == '__main__':
    g = Graph()  # clrs kruskal example
    g.add_edge('a', 'b', weight=4)
    g.add_edge('b', 'c', weight=8)
    g.add_edge('c', 'd', weight=7)
    g.add_edge('c', 'f', weight=4)
    g.add_edge('d', 'e', weight=9)
    g.add_edge('e', 'f', weight=10)
    g.add_edge('f', 'g', weight=10)
    # g.add_edge('g', 'h', weight=10)

    # g.add_edge('a', 'h', weight=8)
    # g.add_edge('b', 'h', weight=11)
    # g.add_edge('c', 'i', weight=2)
    # g.add_edge('d', 'f', weight=14)
    # g.add_edge('f', 'g', weight=2)
    # g.add_edge('g', 'h', weight=1)
    # g.add_edge('g', 'i', weight=6)
    # g.add_edge('h', 'i', weight=7)

    print(mst_brute(g))

    # g = Graph()
    # g.add_edges_from([('a', 'b'), ('c', 'f'), ('c', 'd'), ('b', 'c'), ('d', 'e')])
    # g.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'a')])
    # print(g)
    # print(is_connected(g))
    # print(is_undirected_cyclic(g))

    # clrs Prim example
    g = Graph()
    g.add_edge('a', 'b', 4)
    g.add_edge('a', 'h', 8)
    g.add_edge('b', 'c', 8)
    g.add_edge('b', 'h', 11)
    g.add_edge('c', 'd', 7)
    g.add_edge('c', 'f', 4)
    g.add_edge('c', 'i', 2)
    g.add_edge('i', 'g', 6)
    g.add_edge('i', 'h', 7)
    g.add_edge('f', 'd', 14)
    g.add_edge('f', 'e', 10)
    g.add_edge('f', 'g', 2)
    g.add_edge('e', 'd', 9)
    g.add_edge('g', 'h', 1)
    print(mst_brute(g))
