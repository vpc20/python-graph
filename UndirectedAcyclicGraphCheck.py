from collections import defaultdict, deque

from Graph import Graph


def is_undirected_acyclic_dfs(g):
    def dfs(g, u):
        seen.add(u)
        for v in g.neighbors(u):
            if v not in seen:
                parent[v] = u
                if not dfs(g, v):
                    return False
            elif parent[u] != v:  # cyclic
                return False
        return True

    if not isinstance(g, Graph):
        return False

    seen = set()
    parent = defaultdict()
    for u in g.vertices:
        if u not in seen:
            if not dfs(g, u):
                return False
    return True


def is_undirected_acyclic_bfs(g):
    if not isinstance(g, Graph):
        return False

    seen = set()
    parent = defaultdict()

    queue = deque()
    for u in g.vertices:
        if u not in seen:
            seen.add(u)
            queue = deque([u])
        while queue:
            u = queue.popleft()
            for v in g.neighbors(u):
                if v not in seen:
                    seen.add(v)
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v:  # cyclic
                    return False
    return True


if __name__ == '__main__':
    g = Graph()
    g.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3)])
    print(g)
    assert is_undirected_acyclic_dfs(g) is False

    g = Graph()
    g.add_edges_from([(0, 1), (0, 2), (1, 2)])
    print(g)
    assert is_undirected_acyclic_dfs(g) is False

    g = Graph()
    g.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    print(g)
    assert is_undirected_acyclic_dfs(g) is False

    g = Graph()
    g.add_edges_from([(0, 1)])
    print(g)
    assert is_undirected_acyclic_dfs(g) is True

    g = Graph()
    g.add_edges_from([(0, 1), (0, 2), (1, 3)])
    print(g)
    assert is_undirected_acyclic_dfs(g) is True

    g = Graph()
    g.add_edges_from([(0, 1), (0, 2), (1, 3)])
    print(g)
    assert is_undirected_acyclic_bfs(g) is True
