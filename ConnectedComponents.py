from collections import deque

from DisjointSet import DisjointSet
from Graph import Graph, Digraph
from Transpose import transpose


def is_connected(g):
    """
    An undirected graph is connected if every vertex is reachable from all other vertices.

    :param g: input Graph
    :return: True if the graph is connected, False otherwise.
    """

    def dfs(g, u):
        seen.add(u)
        for v in g.neighbors(u):
            if v not in seen:
                dfs(g, v)

    count = 0
    seen = set()
    for u in g.vertices:
        if u not in seen:
            count += 1  # count connected components
            if count > 1:
                return False
            dfs(g, u)
    return True


def connected_components(g):
    """
    The connected components of a graph are the equivalence classes of vertices under
    the “is reachable from” relation.

    :param g: input Graph
    :return: list of sets contaning the connected vertices
    """

    def dfs(g, u):
        seen.add(u)
        conns[-1].append(u)
        for v in g.neighbors(u):
            if v not in seen:
                dfs(g, v)

    conns = []
    seen = set()
    for u in g.vertices:
        if u not in seen:
            conns.append([])
            dfs(g, u)
    return conns


def connected_components_bfs(g):
    visited = set()
    conns = []
    q = deque()
    for u in g.vertices:
        if u not in visited:
            visited.add(u)
            conns.append([u])
            q.append(u)
        while q:
            u = q.popleft()
            for v in g.neighbors(u):
                if v not in visited:
                    visited.add(v)
                    conns[-1].append(v)
                    q.append(v)
    return conns


def connected_components_dj(g):
    djset = DisjointSet()
    for v in g.vertices:
        djset.make_set(v)

    for v1, v2 in g.edges:
        if djset.find_set(v1) != djset.find_set(v2):
            djset.union(v1, v2)

    return djset.get_set()


def strongly_connected_components(g):
    """
    The strongly connected components of a directed graph are the equivalence classes of
    vertices under the “are mutually reachable” relation.

    :param g: input graph
    :return: list of sets containing the strongly connected vertices
    """

    def dfs(g, u):
        seen.add(u)
        for v in g.neighbors(u):
            if v not in seen:
                dfs(g, v)
        verts.appendleft(u)

    def dfs_gt(gt, u):
        seen.add(u)
        conns[-1].append(u)
        for v in gt.neighbors(u):
            if v not in seen:
                dfs_gt(gt, v)

    seen = set()
    verts = deque()  # vertices in order of decreasing finishing time
    for u in g.vertices:
        if u not in seen:
            dfs(g, u)

    gt = transpose(g)
    seen = set()
    conns = []
    for u in verts:
        if u not in seen:
            conns.append([])
            dfs_gt(gt, u)
    return conns


if __name__ == '__main__':
    g = Graph()
    g.add_edges_from([('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'),
                      ('e', 'f'), ('e', 'g'), ('h', 'i')])
    g.add_vertex('j')
    print(f'connected: {is_connected(g)}')
    # print(connected_components_dj(g))
    print(connected_components(g))
    assert connected_components(g) == [['a', 'b', 'c', 'd'], ['e', 'f', 'g'], ['h', 'i'], ['j']]

    g = Graph()  # clrs Figure B.2(b)
    g.add_edges_from([(1, 2), (1, 5), (2, 5), (3, 6)])
    g.add_vertex(4)
    print(f'connected: {is_connected(g)}')
    print(connected_components_dj(g))
    print(connected_components(g))
    print(connected_components_bfs(g))
    assert connected_components(g) == [[1, 2, 5], [3, 6], [4]]

    g = Graph()
    g.add_edges_from([(1, 2), (1, 5), (2, 3), (2, 5), (3, 6), (4, 5)])
    print(f'connected: {is_connected(g)}')
    # print(connected_components_dj(g))
    print(connected_components(g))
    assert connected_components(g) == [[1, 2, 3, 6, 5, 4]]
    print(connected_components_bfs(g))
    print(connected_components_dj(g))
    assert connected_components_bfs(g) == [[1, 2, 5, 3, 4, 6]]

    dg = Digraph()
    dg.add_edges_from([('a', 'b'), ('b', 'c'), ('b', 'e'), ('c', 'd'), ('c', 'g'), ('d', 'c'), ('d', 'h'),
                       ('e', 'a'), ('e', 'f'), ('f', 'g'), ('g', 'f'), ('g', 'h'), ('h', 'h'), ])
    print(strongly_connected_components(dg))
    assert strongly_connected_components(dg) == [['a', 'e', 'b'], ['c', 'd'], ['g', 'f'], ['h']]

    dg = Digraph()
    dg.add_edges_from([(0, 1), (1, 3), (2, 1), (3, 2), (3, 4), (4, 5), (5, 7), (6, 4), (7, 6)])
    print(strongly_connected_components(dg))
    assert strongly_connected_components(dg) == [[0], [1, 2, 3], [4, 6, 7, 5]]

    dg = Digraph()
    dg.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (3, 4)])
    print(strongly_connected_components(dg))
    assert strongly_connected_components(dg) == [[0], [2], [1], [3], [4]]
