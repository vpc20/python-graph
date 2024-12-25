from collections import defaultdict

from Graph import Graph, Digraph


def has_eulerian_path(g):
    if len(g.vertices) == 1:
        return True

    degree = defaultdict(int)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    for u, v in g.edges:
        if type(g) == Graph:  # undirected graph
            degree[u] += 1
            degree[v] += 1
        else:  # directed graph
            out_degree[u] += 1
            in_degree[v] += 1

    if type(g) == Graph:  # undirected graph
        odd_count = 0
        zero_count = 0
        for u in g.vertices:
            if degree[u] % 2 != 0:
                odd_count += 1
            if degree[u] == 0:
                zero_count += 1
        if odd_count != 0 and odd_count != 2:
            return False
        if zero_count > 0:
            return False
    else:  # directed graph
        start_nodes = 0
        end_nodes = 0
        for u in g.vertices:
            if out_degree[u] - in_degree[u] > 1 or in_degree[u] - out_degree[u] > 1:
                return False
            elif out_degree[u] - in_degree[u] == 1:
                start_nodes += 1
            elif in_degree[u] - out_degree[u] == 1:
                end_nodes += 1
        if not (start_nodes == 0 and end_nodes == 0 or start_nodes == 1 and end_nodes == 1):
            return False
        # if (start_nodes != 0 or end_nodes != 0) and (start_nodes != 1 or end_nodes != 1):
        #     raise ValueError('Graph has no eulerian path')
    return True


if __name__ == '__main__':
    g = Graph()
    g.add_vertices_from([0])
    assert has_eulerian_path(g) is True

    g = Graph()
    g.add_vertices_from([0, 1])
    assert has_eulerian_path(g) is False

    g = Graph()
    g.add_vertices_from([0, 1, 2])
    g.add_edges_from([(0, 1)])
    assert has_eulerian_path(g) is False

    g = Graph()
    g.add_vertices_from([0, 1, 2, 3])
    g.add_edges_from([(0, 1)])
    assert has_eulerian_path(g) is False

    g = Graph()
    g.add_vertices_from([0, 1, 2])
    g.add_edges_from([(0, 1), (1, 2)])
    assert has_eulerian_path(g) is True

    g = Graph()
    g.add_vertices_from([0, 1, 2, 3])
    g.add_edges_from([(0, 1), (1, 2)])
    assert has_eulerian_path(g) is False

    g = Graph()
    g.add_vertices_from([0, 1, 2, 3])
    g.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    assert has_eulerian_path(g) is False

    g = Graph()
    g.add_vertices_from([0, 1, 2, 3])
    g.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)])
    assert has_eulerian_path(g) is True

    g = Graph()
    g.add_vertices_from(list(range(1, 24)))
    g.add_edges_from([(1, 5), (1, 6), (2, 6), (2, 7), (3, 7), (3, 8), (4, 8), (4, 9),
                      (5, 10), (5, 11), (6, 11), (6, 12), (7, 12), (7, 13), (8, 13), (8, 14), (9, 14),
                      (10, 15), (11, 15), (11, 16), (12, 16), (12, 17), (13, 17), (13, 18), (14, 18), (14, 19),
                      (15, 20), (16, 20), (16, 21), (17, 21), (17, 22), (18, 22), (18, 23), (19, 23)])
    assert has_eulerian_path(g) is True

    # dg = Digraph()
    # dg.add_vertices_from([0, 1, 2, 3, 4])
    # dg.add_edges_from([(0, 1), (1, 2), (2, 1), (1, 3), (3, 4)])
    # print(has_eulerian_path(dg))
