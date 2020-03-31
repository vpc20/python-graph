from DisjointSet import DisjointSet
from Graph import Graph


def mst_kruskal(graph):
    djset = DisjointSet()
    mst_weight = 0
    mst_edges = []

    for v in graph.vertices():
        djset.make_set(v)

    edges_by_weight = []
    for v1, v2 in graph.edges():
        edges_by_weight.append((v1, v2, graph.get_weight(v1, v2)))
    edges_by_weight.sort(key=lambda e: e[2])  # sort by weight

    for v1, v2, _ in edges_by_weight:
        if djset.find_set(v1) != djset.find_set(v2):
            djset.union(v1, v2)
            mst_edges.append((v1, v2))
            mst_weight += graph.get_weight(v1, v2)
    return mst_weight, mst_edges


# def mst_kruskal(graph):
#     djset = DisjointSet()
#     mst_weight = 0
#     mst_edges = []
#
#     vertex_seq = defaultdict(str)
#     for i, vertex in enumerate(graph.vertices()):
#         vertex_seq[vertex] = i
#         djset.make_set(i)
#
#     edges_by_weight = []
#     for v1, v2 in graph.edges():
#         edges_by_weight.append((v1, v2, graph.get_weight(v1, v2)))
#     edges_by_weight.sort(key=lambda e: e[2])  # sort by weight
#
#     for v1, v2, _ in edges_by_weight:
#         if djset.find_set(vertex_seq[v1]) != djset.find_set(vertex_seq[v2]):
#             djset.union(vertex_seq[v1], vertex_seq[v2])
#             mst_edges.append((v1, v2))
#             mst_weight += graph.get_weight(v1, v2)
#     return mst_weight, mst_edges

if __name__ == '__main__':
    g = Graph()

    # cp 4.10 in https://visualgo.net/en/mst
    g.adj_list = {0: [1, 4, 3, 2], 1: [0, 2], 4: [0, 3], 3: [0, 2, 4], 2: [0, 1, 3]}
    g.weights = {(0, 1): 4, (1, 0): 4, (1, 2): 2, (2, 1): 2, (2, 3): 8, (3, 2): 8, (3, 4): 9, (4, 3): 9, (0, 4): 6,
                 (4, 0): 6, (0, 3): 6, (3, 0): 6, (0, 2): 4, (2, 0): 4}
    print(mst_kruskal(g))

    # g = complete_graph(10)
    # print(mst_kruskal(g))

    g = Graph()  # clrs kruskal example
    g.add_edge('a', 'b', weight=4)
    g.add_edge('b', 'c', weight=8)
    g.add_edge('c', 'd', weight=7)
    g.add_edge('c', 'f', weight=4)
    g.add_edge('d', 'e', weight=9)
    g.add_edge('e', 'f', weight=10)
    g.add_edge('f', 'g', weight=10)
    # g.add_edge('g', 'h', weight=10)


    print(mst_kruskal(g))
