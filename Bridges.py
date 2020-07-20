from Graph import Graph


def bridges(g):
    def dfs(u, parent):
        nonlocal idno
        seen.add(u)
        idno += 1
        low[u] = ids[u] = idno

        for v in g.neighbors(u):
            if v == parent:
                continue
            if v not in seen:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if ids[u] < low[v]:
                    result.append((u, v))
            else:
                low[u] = min(low[u], ids[v])

    seen = set()
    idno = 0
    ids = {}
    low = {}
    for u in g.vertices:
        ids[u] = 0
        low[u] = 0

    result = []
    for u in g.vertices:
        if u not in seen:
            dfs(u, None)

    return result


if __name__ == '__main__':
    g = Graph()
    g.add_vertices_from([1, 2, 3, 4, 5, 6])
    g.add_edges_from([(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6), (3, 4)])
    # g.add_edges_from([(1, 2), (1, 3), (2, 3)])
    print(g)
    print(bridges(g))
