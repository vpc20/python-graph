import sys
from heapq import heappush, heappop

from Graph import Graph


def mst_prim(graph, root=None):
    def _mst_prim(graph, root):
        mst_weight = 0
        mst_edges = []
        mst_verts = {root}
        visited = {root}
        minq = []
        for nb in graph.neighbors(root):
            if nb not in visited:
                heappush(minq, (graph.weight(root, nb), root, nb))

        while minq:
            wt, vert, nb = heappop(minq)
            if nb not in mst_verts:
                mst_verts.add(nb)
                mst_edges.append((vert, nb))
                mst_weight += graph.weight(vert, nb)
                vert = nb
                for nb in graph.neighbors(vert):
                    if nb not in visited:
                        heappush(minq, (graph.weight(vert, nb), vert, nb))
                visited.add(vert)
        return mst_weight, mst_edges

    if root is None:
        root = next(iter(graph.adj.keys()))

    return _mst_prim(graph, root)


# def mst_prim(graph, root):
#     mst = list()
#     min_wt = dict()
#     parent = dict()
#     for vert in graph.vertices():
#         min_wt[vert] = sys.maxsize
#         parent[vert] = None
#
#     min_wt[root] = 0
#     minq = [[sys.maxsize, vert] for vert in graph.vertices() if vert != root]
#     minq.append([0, root])
#     while minq:
#         vert = min(minq)[1]
#         minq.remove(min(minq))
#         for nb in graph.neighbors(vert):
#             wt = graph.get_weight(vert, nb)
#             if nb in [v for _, v in minq] and wt < min_wt[nb]:
#                 parent[nb] = vert
#                 min_wt[nb] = wt
#                 for i, item in enumerate(minq):
#                     if item[1] == nb:
#                         minq[i][0] = wt
#                         break
#                 mst.append((vert, nb))
#     return mst


def mst_prim_clrs(graph):
    seen = set()
    min_wt = dict()
    parent = dict()
    for v in graph.vertices():
        min_wt[v] = sys.maxsize
        parent[v] = None

    root = graph.vertices()[0]  # take first vertex as root
    min_wt[root] = 0
    minq = [(0, root)]
    while minq:
        _, u = heappop(minq)
        for v in graph.neighbors(u):
            if (u, v) not in seen:
                ewt = graph.weight(u, v)
                if ewt < min_wt[v]:
                    parent[v] = u
                    min_wt[v] = ewt
                    heappush(minq, (ewt, v))
                seen.add((u, v))
                seen.add((v, u))
    # create mst
    parent.pop(root)  # initial value not required in mst
    mst = Graph()
    for v, u in parent.items():
        mst.add_edge(u, v, g.weight(u, v))
    return mst


# def mst_prim_clrs(graph, root):
#     mst_wt = 0
#     mst_edges = list()
#     min_wt = dict()
#     parent = dict()
#     for vert in graph.vertices():
#         min_wt[vert] = sys.maxsize
#         parent[vert] = None
#
#     min_wt[root] = 0
#     minq = [[sys.maxsize, vert] for vert in graph.vertices() if vert != root]
#     heappush(minq, [0, root])
#     prev_vert = None
#     while minq:
#         vert = heappop(minq)[1]
#         if prev_vert:
#             mst_edges.append((prev_vert, vert))
#             mst_wt += graph.get_weight(prev_vert, vert)
#         prev_vert = vert
#         for nb in graph.neighbors(vert):
#             wt = graph.get_weight(vert, nb)
#             if nb in [v for _, v in minq] and wt < min_wt[nb]:
#                 parent[nb] = vert
#                 min_wt[nb] = wt
#                 for i, item in enumerate(minq):
#                     if item[1] == nb:
#                         minq[i][0] = wt
#                         heapify(minq)
#                         break
#     return mst_wt, mst_edges

if __name__ == '__main__':
    g = Graph()

    # cp 4.10 in https://visualgo.net/en/mst
    # g.adj_list = {0: [1, 4, 3, 2], 1: [0, 2], 4: [0, 3], 3: [0, 2, 4], 2: [0, 1, 3]}
    # g.weights = {(0, 1): 4, (1, 0): 4, (1, 2): 2, (2, 1): 2, (2, 3): 8, (3, 2): 8, (3, 4): 9, (4, 3): 9, (0, 4): 6,
    #              (4, 0): 6, (0, 3): 6, (3, 0): 6, (0, 2): 4, (2, 0): 4}
    # print(mst_prim(g))
    # print(mst_prim_clrs(g, 0))

    # clrs Prim example
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

    print(mst_prim_clrs(g))

    # print(mst_prim_clrs(g, 'a'))
    # print([(v, k) for k, v in mst_prim_clrs(g, 'a').items()])
    # for k, v in mst_prim_clrs(g, 'a').items():
    #     print(k, v)

    # print(mst_prim(g, 'a'))
