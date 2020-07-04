from collections import defaultdict, deque
from itertools import combinations

from DisjointSet import DisjointSet


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.weights = {}

    def __str__(self):
        return str(self.adj)[28:-1]

    @property
    def vertices(self):
        return list(self.adj.keys())

    @property
    def edges(self):
        eset = set()
        for v in self.vertices:
            for nb in self.neighbors(v):
                if (nb, v) not in eset:
                    eset.add((v, nb))
        return list(eset)

    def neighbors(self, vertex):
        return self.adj[vertex]

    def all_weights(self):
        return [((u, v), self.weight(u, v)) for u, v in self.edges]

    def weight(self, v1, v2):
        if (v1, v2) in self.weights:
            return self.weights[(v1, v2)]
        elif (v2, v1) in self.weights:
            return self.weights[(v2, v1)]
        else:
            return 0

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def remove_vertex(self, vertex):
        self.adj.pop(vertex)
        for k, v in self.adj.items():
            if vertex in v:
                self.adj[k].remove(vertex)

    def add_edge(self, u, v, weight=1):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight

    def add_edges_from(self, edges_arr):
        for u, v in edges_arr:
            self.add_edge(u, v)

    def add_weighted_edges_from(self, edges_arr):
        for u, v, w in edges_arr:
            self.add_edge(u, v, w)

    def add_single_edge(self, u, v, weight=1):
        self.adj[u].append(v)
        self.weights[(u, v)] = weight

    def remove_edge(self, u, v):
        self.adj[u].remove(v)
        self.adj[v].remove(u)
        self.weights.pop((u, v))
        self.weights.pop((v, u))


class Digraph(Graph):
    def __init__(self):
        super().__init__()

    @property
    def edges(self):
        return [(v, nb) for v in self.vertices for nb in self.neighbors(v)]

    def add_edge(self, u, v, weight=1):
        self.adj[u].append(v)
        if v not in self.adj:
            self.adj[v] = []
        self.weights[(u, v)] = weight

    def add_edges_from(self, edges):
        for u, v in edges:
            self.add_edge(u, v)

    def add_weighted_edges_from(self, edges):
        for u, v, w in edges:
            self.add_edge(u, v, w)

    def remove_edge(self, u, v):
        self.adj[u].remove(v)
        self.weights.pop((u, v))


def complete_graph(n, alpha=False):
    g = Graph()
    if n == 1:
        if alpha:
            g.add_vertex('a')
        else:
            g.add_vertex(0)
    for i in range(n):
        for j in range(i + 1, n):
            if alpha:
                g.add_edge(chr(i + 97), chr(j + 97))
            else:
                g.add_edge(i, j)
    return g


def path_graph(n):
    g = Graph()
    if n == 1:
        g.add_vertex(0)
    for i in range(1, n):
        g.add_edge(i - 1, i)
    return g


def circular_graph(n):
    g = path_graph(n)
    g.add_edge(n - 1, 0)
    return g


def grid_2d_graph(rows, cols):
    g = Graph()
    # add edge for each row
    for i in range(1, rows * cols):
        if i % cols != 0:
            g.add_edge(i - 1, i)
    # add edge for each col
    for i in range(rows * cols - cols):
        g.add_edge(i, i + cols)
    return g


def gen_all_graphs(nverts):
    edges = []
    for i in range(nverts):
        for j in range(i + 1, nverts + 1):
            edges.append((i, j))
    for r in range(1, len(edges) + 1):
        for comb in combinations(edges, r):
            # print(comb)
            g = Graph()
            g.add_edges_from(comb)
            yield g


# def is_cyclic(graph):  # dfs traversal
#     visited = set()
#     node_stack = []
#     for vertex in graph.vertices():
#         if vertex not in visited:
#             visited.add(vertex)
#             node_stack.append(vertex)
#             if _is_cyclic(graph, vertex, visited, node_stack):
#                 return True
#             node_stack.pop()
#     return False
#
#
# def _is_cyclic(graph, vertex, visited, node_stack):
#     for neighbor in graph.adj_list[vertex]:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             node_stack.append(neighbor)
#             if _is_cyclic(graph, neighbor, visited, node_stack):
#                 return True
#             node_stack.pop()
#         else:
#             if neighbor in node_stack:
#                 return True


def is_connected(g):
    """
    An undirected graph is connected if every vertex is reachable from all other vertices.

    :param g: undirected graph
    :return: True if the the graph is connected, otherwise False
    """
    gverts = g.vertices
    vset = set(gverts)
    queue = [gverts[0]]
    vset.remove(gverts[0])

    while queue:
        v = queue.pop(0)
        for nb in g.neighbors(v):
            if nb in vset:
                queue.append(nb)
                vset.remove(nb)
    return len(vset) == 0

    # gverts = g.vertices()
    # vset = set(gverts)
    # v = gverts[0]
    #
    # queue = [v]
    # visited = {v}
    # vset.remove(v)
    #
    # while queue:
    #     v = queue.pop(0)
    #     for nb in g.neighbors(v):
    #         if nb not in visited:
    #             queue.append(nb)
    #             visited.add(nb)
    #             vset.remove(nb)
    # return len(vset) == 0


# def is_undirected_cyclic(g):
#     djset = DisjointSet()
#
#     for v in g.vertices:
#         djset.make_set(v)
#
#     eset = set()
#     for v1, v2 in g.edges:
#         if (v2, v1) not in eset:
#             eset.add((v1, v2))
#
#     for v1, v2 in eset:
#         if djset.find_set(v1) != djset.find_set(v2):
#             djset.union(v1, v2)
#         else:
#             return True
#     return False


# def is_undirected_cyclic(g):
#     djset = DisjointSet()
#
#     for v in g.vertices():
#         djset.make_set(v)
#
#     edges = g.edges()
#     for v1, v2 in edges:
#         if djset.find_set(v1) != djset.find_set(v2):
#             djset.union(v1, v2)
#             edges.remove((v2, v1))
#         else:
#             return True
#     return False


# def is_directed_cyclic(g):  # dfs traversal
#     def _is_cyclic(graph, v):
#         cycle_stack.append(v)
#         for neighbor in graph.neighbors(v):
#             if neighbor in cycle_stack:
#                 return True
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 if _is_cyclic(graph, neighbor):
#                     return True
#         cycle_stack.pop()
#
#     visited = set()
#     cycle_stack = []
#     for v in g.vertices:
#         if v not in visited:
#             visited.add(v)
#             if _is_cyclic(g, v):
#                 return False
#     return False


# def is_directed_cyclic_bfs(g):
#     visited = set()
#     queue = []
#     for v in g.vertices():
#         if v not in visited:
#             queue = [v]
#             visited.add(v)
#         cycles = set()
#         while queue:
#             vertex = queue.pop(0)
#             cycles.add(vertex)
#             for nb in g.neighbors(vertex):
#                 if nb in cycles:
#                     return True
#                 if nb not in visited:
#                     queue.append(nb)
#                     visited.add(nb)
#     return False


def is_forest(g):
    """
    A forest is an acyclic, undirected graph.

    :param g: undirected graph
    :return: True if graph is a forest, otherwise False
    """
    if not isinstance(g, Graph):
        return False

    djset = DisjointSet()

    for v in g.vertices:
        djset.make_set(v)

    eset = set()
    for v1, v2 in g.edges:
        if (v2, v1) not in eset:
            eset.add((v1, v2))

    for v1, v2 in eset:
        if djset.find_set(v1) != djset.find_set(v2):
            djset.union(v1, v2)
        else:
            return False
    return True


def is_tree(g):
    """
    A tree is a connected forest.

    :param g: undirected graph
    :return: True if graph is a tree, otherwise False
    """
    return is_forest(g) and is_connected(g)


def is_spanning_tree(g, edges):
    """
    The spanning tree is a set of edges which connects all of the vertices to form a tree
    (an acyclic graph). The spanning tree with the smallest total weight of edges is the
    minimum spanning tree.

    :param g: input graph
    :param edges: list of edges for spanning tree checking
    """
    vset = set(g.vertices)
    for v1, v2 in edges:
        if v1 in vset:
            vset.remove(v1)
        if v2 in vset:
            vset.remove(v2)
    if len(vset) != 0:
        return False

    g1 = Graph()
    g1.add_edges_from(edges)
    return is_connected(g1) and not is_undirected_cyclic(g1)


def is_bipartite_bfs(graph):
    """
    A bipartite graph is an undirected graph G = (V, E) in which V can be partitioned into
    two sets V1 and V2 such that (u, v) ∈ E implies either u ∈ V1 and v ∈ V2 or
    u ∈ V2 and v ∈ V1. That is, all edges go between the two sets V1 and V2.

    :param graph: input graph
    :return: True if the the graph is bipartite, otherwise False
    """
    visited = set()
    colors = defaultdict(int)
    curr_color = 0
    queue = deque()
    for vertex in graph.vertices:
        if vertex not in visited:
            colors[vertex] = curr_color
            queue.append(vertex)
            visited.add(vertex)
        while queue:
            vertex = queue.popleft()
            curr_color = 1 - colors[vertex]  # switch color
            for neighbor in graph.neighbors(vertex):
                if neighbor not in visited:
                    colors[neighbor] = curr_color
                    queue.append(neighbor)
                    visited.add(neighbor)
                else:
                    if colors[neighbor] == colors[vertex]:
                        return False
    return True


def is_bipartite_dfs(graph):
    def _is_bipartite(vertex):
        curr_color = 1 - colors[vertex]
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                colors[neighbor] = curr_color
                visited.add(neighbor)
                if not _is_bipartite(neighbor):
                    return False
            else:
                if colors[neighbor] != curr_color:
                    return False
        return True

    visited = set()
    for vertex in graph.vertices:
        if vertex not in visited:
            colors = {vertex: 0}
            visited.add(vertex)
            return _is_bipartite(vertex)
    return True


# def is_vertex_cover(graph, vertex_list):
#     edge_list = []
#     for vertex in vertex_list:
#         for edge in graph.edges():
#             if vertex in edge and edge not in edge_list:
#                 edge_list.append(edge)
#     return sorted(edge_list) == sorted(graph.edges())


def is_vertex_cover(graph, vlist):
    """
    A vertex cover of an undirected graph G = (V, E) is a subset V' ⊆ V such that if
    (u, v) ∈ E, then u ∈ V' or v ∈ V' (or both). That is, each vertex “covers” its
    incident edges, and a vertex cover for G is a set of vertices that covers all the edges
    in E.

    :param graph: input graph
    :param vlist: list of vertices for checking vertex cover
    :return: True if the set of vertices is a vertex cover, otherwise False
    """
    edge_list = graph.edges
    for vertex in vlist:
        i = 0
        while edge_list and i < len(edge_list):
            if vertex in edge_list[i]:
                edge_list.pop(i)
                i -= 1
            i += 1
    return len(edge_list) == 0


def min_vertex_cover_brute(graph):
    for r in range(1, len(graph.vertices) + 1):
        for comb in combinations(graph.vertices, r):
            if is_vertex_cover(graph, comb):
                return comb
    return ()


def approx_vertex_cover(graph):
    vcover_list = []  # list of vertices
    edges_list = graph.edges
    while edges_list:
        v1, v2 = edges_list[0]
        vcover_list.append(v1)
        vcover_list.append(v2)
        i = 0
        while i < len(edges_list):
            if v1 in edges_list[i] or v2 in edges_list[i]:
                edges_list.pop(i)
                i -= 1
            i += 1
    return vcover_list


def list_edges(graph, vertex_list):
    edge_list = []
    for edge in graph.edges:
        if edge[0] in vertex_list and edge[1] in vertex_list and edge not in edge_list:
            edge_list.append(edge)
    return edge_list


def complete_edges(vertex_list):
    edge_list = []
    for i in range(len(vertex_list)):
        for j in range(i + 1, len(vertex_list)):
            edge_list.append((vertex_list[i], vertex_list[j]))
            edge_list.append((vertex_list[j], vertex_list[i]))
    return edge_list


def is_clique(graph, vlist):
    """
    A clique in an undirected graph G = (V, E) is a subset V' ⊆ V of vertices, each
    pair of which is connected by an edge in E. In other words, a clique is a complete
    subgraph of G.

    :param graph: input graph
    :param vlist: list of vertices for clique checking
    :return: True if the list of vertices forms a clique, otherwise False
    """
    return sorted(list_edges(graph, vlist)) == sorted(complete_edges(vlist))


def clique(graph):
    for i in range(len(graph.vertices) + 1, 1, -1):
        for comb in combinations(graph.vertices, i):
            if is_clique(graph, comb):
                return comb
    return None


def is_independent_set(graph, vlist):
    """
    An independent set of a graph G = (V, E) is a subset V' ⊆ V of vertices such
    that each edge in E is incident on at most one vertex in V'. The independent-set
    problem is to find a maximum-size independent set in G.

    :param graph: input graph
    :param vlist:
    :return: True if the list of vertices forms an independent set, otherwise Fals
    """
    for vertex in vlist:
        for v1, v2 in graph.edges:
            if (vertex == v1 and v2 in vlist) or \
                    (vertex == v2 and v1 in vlist):
                return False
    return True


def independent_set(graph):
    for i in range(len(graph.vertices) + 1, 0, -1):
        for comb in combinations(graph.vertices, i):
            if is_independent_set(graph, set(comb)):
                return comb
    return None


def inverse_graph(g):
    all_edges = complete_edges(g.vertices)
    inverse_edges = list(set(all_edges) - set(g.edges))
    invg = Graph()
    for edge in inverse_edges:
        invg.add_single_edge(edge[0], edge[1])
    other_vertices = set(g.vertices) - set(invg.vertices)  # vertices without edge
    for v in other_vertices:
        invg.add_vertex(v)
    return invg



def articulation_point(g):
    def _articulation_point(g, v):
        nonlocal time
        children = 0
        dtime[v] = time
        low[v] = time
        time += 1
        for nb in g.neighbors(v):
            if nb not in visited:
                visited.add(nb)
                parent[nb] = v
                children += 1
                _articulation_point(g, nb)
                low[v] = min(low[v], low[nb])
                if v not in parent and children > 1:  # root vertex
                    art_pts.append(v)
                if v in parent and low[nb] >= dtime[v]:  # non-root vertex
                    art_pts.append(v)
            elif nb != parent[v]:
                low[v] = min(low[v], dtime[nb])

    visited = set()
    time = 0
    dtime = {}
    low = {}
    parent = {}
    art_pts = []
    for v in g.vertices:
        if v not in visited:
            visited.add(v)
            _articulation_point(g, v)
    return art_pts


if __name__ == '__main__':
    g = Graph()

    g.add_edge('a', 'b')
    g.add_edge('a', 'd')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('c', 'e')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')
    g.add_edge('e', 'g')
    g.add_edge('f', 'g')
    g.add_edge('x', 'y')
    g.add_edge('x', 'z')

    print(is_directed_cyclic(g))

    # g.add_edge('a', 'b')
    # g.add_edge('a', 'c')
    # g.add_edge('b', 'c')
    # g.add_edge('b', 'd')
    # g.add_edge('b', 'e')
    # g.add_edge('b', 'f')
    # g.add_edge('c', 'e')
    # g.add_edge('c', 'f')
    # g.add_edge('d', 'e')
    # g.add_edge('e', 'f')
    #
    # print('Graph:', g)
    # print('Vertices:', g.vertices())
    # print('Edges:', g.edges())
    # print(g.weights)
    # print('')

    # # print('vertex cover', vertex_cover(g))
    # # print('')
    # # print(is_vertex_cover(g, ['b', 'a', 'e', 'f']))
    #
    # # print('clique', clique(g))
    # # print('')
    # # print('clique', is_clique(g, ['a', 'b', 'c']))
    #
    # print('independent set', independent_set(g))
    # print('')
    #
    # print('inverse graph')
    # ig = inverse_graph(g)
    # print('Graph:', ig)
    # print('Vertices:', ig.vertices())
    # print('Edges:', ig.edges())
    # print('')
    #
    # # bfs_print_vertices(g)
    # # print('')
    #
    # # print('shortest path')
    # # print(bfs_shortest_path(g, 'a', 'e'))
    # # print('')
    #
    # print('dfs_print_vertices')
    # dfs_print_vertices(g)
    # print('')
    # print('dfs_print_vertices_iterative')
    # dfs_print_vertices_iterative(g)
    # print('')
    # print('bfs_print_vertices')
    # bfs_print_vertices(g)
    # print('')
    #
    # print(dfs_connection_dict(g))
    # print('')
    #
    # # print(dfs_predecessors(g, 'a'))
    # # print(dfs_path(g, 'd', 'a'))
    # # print(g.neighbors('a'))
    #
    # # print(bfs_all_paths(g, 'a', 'd'))
    # print('dfs all paths')
    # print(dfs_all_paths(g, 'a', 'b'))
    # print('')
    #
    # # pg = path_graph(3)
    # # print(bfs_all_paths(cg, 0, 2))
    #
    # # print('')
    # # pg = path_graph(5)
    # # print('Path Graph:', pg)
    # # print('Vertices:', pg.vertices())
    # # print('Edges:', pg.edges())
    # # print('')
    # #
    # # cirg = circular_graph(5)
    # # print('Circular Graph:', cirg)
    # # print('Vertices:', cirg.vertices())
    # # print('Edges:', cirg.edges())
    # # print('')
    # #
    # # cg = complete_graph(5)
    # # print('Complete Graph:', cg)
    # # print('Vertices:', cg.vertices())
    # # print('Edges:', cg.edges())
    # # print('')
    # #
    # # gg = grid_2d_graph(3, 4)
    # # print('Grid 2d Graph:', gg)
    # # print('Vertices:', gg.vertices())
    # # print('Edges:', sorted(gg.edges()))
    # # print('')
    g = Graph()
    g.add_edge('a', 'b')
    # dg.add_edge('c', 'd')
    g.add_vertex('c')
    print(g)
    invg = inverse_graph(g)
    print(invg)

    g = complete_graph(10)
    print(g)
    print(len(g.edges))
    g = grid_2d_graph(2, 3)
    print(g)

    g = circular_graph(4)
    print(g)
    print(g.weights)
    # g.remove_edge(0, 3)
    # print(g)
    # print(g.weights)
    g.remove_vertex(3)
    print(g)
    print(g.weights)

    g = complete_graph(10, alpha=True)
    print(g)
    print(len(g.edges))

    # g = Graph()  # clrs kruskal example
    # g.add_edge('a', 'b', weight=4)
    # g.add_edge('a', 'h', weight=8)
    # g.add_edge('b', 'c', weight=8)
    # g.add_edge('b', 'h', weight=11)
    # g.add_edge('c', 'd', weight=7)
    # g.add_edge('c', 'f', weight=4)
    # g.add_edge('c', 'i', weight=2)
    # g.add_edge('d', 'e', weight=9)
    # g.add_edge('d', 'f', weight=14)
    # g.add_edge('e', 'f', weight=10)
    # g.add_edge('f', 'g', weight=2)
    # g.add_edge('g', 'h', weight=1)
    # g.add_edge('g', 'i', weight=6)
    # g.add_edge('h', 'i', weight=7)
    #
    # print(is_connected(g))

    g = Graph()  # clrs kruskal example
    g.add_edge('a', 'b', weight=4)
    g.add_edge('b', 'c', weight=8)
    g.add_edge('c', 'd', weight=7)
    # g.add_edge('c', 'f', weight=4)
    # g.add_edge('d', 'e', weight=9)
    # g.add_edge('e', 'f', weight=10)

    print(is_undirected_cyclic(g))
    print(is_spanning_tree(g, [('a', 'b'), ('c', 'd')]))

    # print(gen_all_graphs(5))

    g1 = Graph()
    g1.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'a')])
    # g1.add_edges_from([('a', 'b'), ('b', 'c')])
    print(g1)
    print(is_undirected_cyclic(g1))

    dg = Digraph()
    dg.add_edge('a', 'b')
    dg.add_edge('a', 'c')
    print(dg)
    print(dg.edges)
    print(is_directed_acyclic(dg))

    g = Graph()
    # g.add_vertex(0)

    # g.add_edge(0, 1)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    print(is_forest(g))
    print(is_tree(g))

    # g1 = Graph()
    # g1.add_edges_from([('a', 'b'), ('c', 'd')])
    # print(is_connected(g1))
