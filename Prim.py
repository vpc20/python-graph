import sys
from heapq import heappush, heappop, heapify

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
                heappush(minq, (graph.get_weight(root, nb), root, nb))

        while minq:
            wt, vert, nb = heappop(minq)
            if nb not in mst_verts:
                mst_verts.add(nb)
                mst_edges.append((vert, nb))
                mst_weight += graph.get_weight(vert, nb)
                vert = nb
                for nb in graph.neighbors(vert):
                    if nb not in visited:
                        heappush(minq, (graph.get_weight(vert, nb), vert, nb))
                visited.add(vert)
        return mst_weight, mst_edges

    if root is None:
        root = next(iter(graph.adj_list.keys()))

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


def mst_prim_clrs(graph, root):
    mst_wt = 0
    mst_edges = list()
    min_wt = dict()
    parent = dict()
    for vert in graph.vertices():
        min_wt[vert] = sys.maxsize
        parent[vert] = None

    min_wt[root] = 0
    minq = [[sys.maxsize, None, vert] for vert in graph.vertices() if vert != root]
    heappush(minq, [0, None, root])
    while minq:
        _, prev_vert, vert = heappop(minq)
        if not prev_vert:
            vert = root
        else:
            mst_edges.append((prev_vert, vert))
            mst_wt += graph.get_weight(prev_vert, vert)
        for nb in graph.neighbors(vert):
            wt = graph.get_weight(vert, nb)
            if nb in [v for _, _, v in minq] and wt < min_wt[nb]:
                parent[nb] = vert
                min_wt[nb] = wt
                for i, item in enumerate(minq):
                    if item[2] == nb:
                        minq[i][1] = vert
                        minq[i][0] = wt
                        heapify(minq)
                        break
    return mst_wt, mst_edges


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
    g.adj_list = {0: [1, 4, 3, 2], 1: [0, 2], 4: [0, 3], 3: [0, 2, 4], 2: [0, 1, 3]}
    g.weights = {(0, 1): 4, (1, 0): 4, (1, 2): 2, (2, 1): 2, (2, 3): 8, (3, 2): 8, (3, 4): 9, (4, 3): 9, (0, 4): 6,
                 (4, 0): 6, (0, 3): 6, (3, 0): 6, (0, 2): 4, (2, 0): 4}
    print(mst_prim(g))
    print(mst_prim_clrs(g, 0))
