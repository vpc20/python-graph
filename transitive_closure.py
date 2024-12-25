from Graph import Digraph


def transitive_closure(g):
    """
    Given a directed graph G = (V, E) with vertex set V = {1,2,...,n}, we might
    wish to determine whether G contains a path from i to j for all vertex pairs
    i, j ∈ V. We define the transitive closure of G as the graph G* = (V, E*), where
    E* = {i, j): there is a path from vertex i to vertex j in G}.

    :param g: input directed graph
    :return: transitive closure
    """
    n = len(g.vertices())
    edges = g.edges()
    t = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or (i + 1, j + 1) in edges:
                t[i][j] = 1
    for k in range(1, n + 1):
        for i in range(n):
            for j in range(n):
                t[i][j] = t[i][j] or (t[i][k - 1] and t[k - 1][j])
    return t


# def transitive_closure(g):
#     n = len(g.vertices())
#     edges = g.edges()
#     t = [[[0] * n for _ in range(n)] for _ in range(n + 1)]
#     for i in range(n):
#         for j in range(n):
#             if i == j or (i + 1, j + 1) in edges:
#                 t[0][i][j] = 1
#     for k in range(1, n + 1):
#         for i in range(n):
#             for j in range(n):
#                 t[k][i][j] = t[k - 1][i][j] or (t[k - 1][i][k - 1] and t[k - 1][k - 1][j])
#     return t


if __name__ == '__main__':
    dg = Digraph()
    dg.add_edge(2, 3)
    dg.add_edge(2, 4)
    dg.add_edge(3, 2)
    dg.add_edge(4, 1)
    dg.add_edge(4, 3)

    print(dg)
    print(dg.edges())
    t = transitive_closure(dg)

    # for i, tc in enumerate(t):
    #     print(f't[{i}]')
    #     for row in tc:
    #         print(row)

    for row in t:
        print(row)
