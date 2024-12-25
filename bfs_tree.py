from collections import defaultdict

from Graph import Graph, Digraph


def bfs_tree(g, src):
    tree = Graph()
    tree.add_vertex(src)
    seen = {src}
    q = [src]
    while q:
        u = q.pop(0)
        for v in g.neighbors(u):
            if v not in seen:
                tree.add_edge(u, v)
                q.append(v)
                seen.add(v)
    return tree


# def bfs_tree(g, src):
#     pred = {}  # predecessors
#     for v in g.vertices:
#         pred[v] = None
#     del pred[src]  # (None --> src) edge not included in tree
#
#     seen = {src}
#     q = [src]
#     while q:
#         u = q.pop(0)
#         for v in g.neighbors(u):
#             if v not in seen:
#                 pred[v] = u
#                 q.append(v)
#                 seen.add(v)
#
#     tree = Graph()
#     tree.add_vertex(src)
#     for v, u in pred.items():
#         if u is not None:
#             tree.add_edge(u, v)
#     return tree


if __name__ == '__main__':
    # g = Graph()
    # g.add_edges_from([('r', 's'), ('r', 'v'), ('s', 'w'), ('t', 'u'), ('t', 'w'),
    #                   ('t', 'x'), ('u', 'x'), ('u', 'y'), ('w', 'x'), ('x', 'y')])
    # t = bfs_tree(g, 'r')
    # print(t)
    # print(sorted(t.edges))
    # bfs print vertices r s v w t x u y
    # [('r', 's'), ('r', 'v'), ('s', 'w'), ('t', 'u'), ('w', 't'), ('w', 'x'), ('x', 'y')]

    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    print(g)

    t = bfs_tree(g, 0)
    print(t)
    print(t.vertices)
    print(t.edges)
