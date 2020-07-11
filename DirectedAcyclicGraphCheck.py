import sys
from collections import defaultdict, deque

from Graph import Digraph

WHITE = 0  # undiscovered
GRAY = 1  # discovered
BLACK = 2  # finished


def is_directed_acyclic_graph(g):
    """
    A directed acyclic graph is a directed graph with no cycles.

    :param g: directed graph
    :return: True if graph is a DAG, otherwise False
    """

    def dfs(g, u):
        colors[u] = GRAY
        for v in g.neighbors(u):
            if colors[v] == WHITE:
                if not dfs(g, v):
                    return False
            elif colors[v] == GRAY:  # back edge
                return False
        colors[u] = BLACK
        return True

    if not isinstance(g, Digraph):
        return False

    colors = {u: WHITE for u in g.vertices}  # vertex colors

    for u in g.vertices:
        if colors[u] == WHITE:
            if not dfs(g, u):
                return False
    return True


def is_directed_acyclic_dfs(g):
    def dfs(g, u):
        seen.add(u)
        cycles.add(u)
        for v in g.neighbors(u):
            if v not in seen:
                if not dfs(g, v):
                    return False
            elif v in cycles:  # back edge
                return False
        cycles.remove(u)
        return True

    if not isinstance(g, Digraph):
        return False

    seen = set()
    cycles = set()
    for u in g.vertices:
        if u not in seen:
            if not dfs(g, u):
                return False
    return True


def is_directed_acyclic_dfs_iter(g):
    seen = set()
    cycles = set()
    stack = []
    for u in g.vertices:
        if u not in seen:
            seen.add(u)
            stack = [u]
            cycles.clear()
        while stack:
            u = stack.pop()
            cycles.add(u)
            for v in g.neighbors(u):
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
                elif v in cycles:
                    return False
    return True


# def is_directed_acyclic_bfs(g):
#     seen = set()
#     levels = {}
#     lvl = 1
#     queue = deque()
#     for u in g.vertices:
#         if u not in seen:
#             queue = deque([u])
#             seen.add(u)
#             levels.clear()
#             levels[u] = 1
#         while queue:
#             lvl += 1
#             for _ in range(len(queue)):
#                 u = queue.popleft()
#                 for v in g.neighbors(u):
#                     if v not in seen:
#                         queue.append(v)
#                         seen.add(v)
#                         levels[v] = lvl
#                     else:
#                         if v in levels and levels[u] < levels[v]:
#                             return False
#     return True


def is_directed_acyclic_bfs2(g):
    dtime = {}  # discovery time
    for u in g.vertices:
        dtime[u] = sys.maxsize
    dtime[g.vertices[0]] = 0

    seen = set()
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
                    dtime[v] = dtime[u] + 1
                    queue.append(v)
                elif dtime[u] >= dtime[v]:
                    return False
    return True


def is_directed_acyclic_bfs(g):
    if not isinstance(g, Digraph):
        return False

    visited = 0
    in_degrees = defaultdict(int)
    for u in g.vertices:
        in_degrees[u] += 0
    for _, v in g.edges:
        in_degrees[v] += 1

    q = deque([k for k, v in in_degrees.items() if v == 0])
    while q:
        u = q.popleft()
        visited += 1
        for v in g.neighbors(u):
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                q.append(v)
    return visited == len(g.vertices)


if __name__ == '__main__':
    dress_order = [['shirt', 'tie'], ['tie', 'jacket'], ['belt', 'jacket'], ['shirt', 'belt'],
                   ['undershorts', 'pants'], ['pants', 'shoes'], ['socks', 'shoes']]
    g = Digraph()
    g.add_edges_from(dress_order)
    g.add_vertex('jacket')
    g.add_vertex('watch')
    g.add_vertex('shoes')
    print(g)
    print(is_directed_acyclic_graph(g))
    print(is_directed_acyclic_dfs(g))
    # print(is_directed_acyclic_bfs(g))

    # g1 = Digraph()
    # g1.add_vertex(1)
    # g1.add_vertex(2)
    # print(is_directed_acyclic_bfs(g1))

    # g2 = Digraph()
    # g2.add_edge(1, 2)
    # g2.add_edge(1, 3)
    # print(is_directed_acyclic_bfs(g2))

    g3 = Digraph()
    g3.add_vertices_from([0, 1, 2])
    g3.add_edges_from([(0, 1), (0, 2), (1, 2)])
    assert is_directed_acyclic_bfs(g3) is True
    # assert is_directed_acyclic_dfs_iter(g3) is True
    assert is_directed_acyclic_bfs2(g3) is True

    g4 = Digraph()
    g4.add_edges_from([(0, 1), (1, 0)])
    assert is_directed_acyclic_bfs(g4) is False
    assert is_directed_acyclic_dfs_iter(g4) is False
    assert is_directed_acyclic_bfs2(g4) is False

    g6 = Digraph()
    g6.add_vertices_from([0, 1])
    g6.add_edges_from([(0, 1)])
    assert is_directed_acyclic_dfs(g6) is True
    assert is_directed_acyclic_dfs_iter(g6) is True
    assert is_directed_acyclic_bfs2(g6) is True
