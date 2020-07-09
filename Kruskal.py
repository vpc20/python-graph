from DisjointSet import DisjointSet
from Graph import Graph


def mst_kruskal(g):
    djset = DisjointSet()
    mst = Graph()

    for u in g.vertices:
        djset.make_set(u)

    for u, v in sorted(g.edges, key=lambda e: g.weight(e[0], e[1])):
        if djset.find_set(u) != djset.find_set(v):
            djset.union(u, v)
            mst.add_edge(u, v, g.weight(u, v))
    return mst


if __name__ == '__main__':
    g = Graph()
    g.add_weighted_edges_from([('a', 'b', 4), ('a', 'h', 8), ('b', 'c', 8), ('b', 'h', 11), ('c', 'd', 7),
                               ('c', 'f', 4), ('c', 'i', 2), ('i', 'g', 6), ('i', 'h', 7), ('f', 'd', 14),
                               ('f', 'e', 10), ('f', 'g', 2), ('e', 'd', 9), ('g', 'h', 1)])
    mst = mst_kruskal(g)
    print(mst.edges)
    print(sum([mst.weight(u, v) for u, v in mst.edges]))

