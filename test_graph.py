from unittest import TestCase

from Graph import *
# from Graph import Graph, Digraph, is_directed_cyclic, is_vertex_cover, min_vertex_cover_brute, is_bipartite_bfs, \
#     is_bipartite_dfs, approx_vertex_cover, articulation_point, is_directed_cyclic_bfs, is_directed_acyclic, is_forest
from Dfs import dfs


class TestGraph(TestCase):
    def test_vertices(self):
        g = Graph()
        g.add_edge('a', 'b')
        g.add_edge('b', 'c')
        g.add_edge('c', 'a')
        self.assertEqual(['a', 'b', 'c'], g.vertices())

    def test_neighbors(self):
        g = Graph()
        g.add_edge('a', 'b')
        g.add_edge('b', 'c')
        g.add_edge('c', 'a')
        self.assertEqual(['b', 'c'], g.neighbors('a'))

    def test_edges(self):
        g = Graph()
        g.add_edge('a', 'b')
        g.add_edge('b', 'c')
        g.add_edge('c', 'a')
        self.assertEqual(sorted([('a', 'b'), ('b', 'a'),
                                 ('b', 'c'), ('c', 'b'),
                                 ('c', 'a'), ('a', 'c')]), sorted(g.edges()))

    def test_get_weight(self):
        g = Graph()
        g.add_edge('a', 'b')
        g.add_edge('b', 'c')
        g.add_edge('c', 'a')
        self.assertEqual(1, g.get_weight('a', 'b'))
        self.assertEqual(1, g.get_weight('b', 'a'))
        self.assertEqual(1, g.get_weight('b', 'c'))
        self.assertEqual(1, g.get_weight('c', 'b'))
        self.assertEqual(1, g.get_weight('c', 'a'))
        self.assertEqual(1, g.get_weight('a', 'c'))

        g = Graph()
        g.add_edge('a', 'b')
        g.add_edge('b', 'c', weight=5)
        g.add_edge('c', 'a')
        self.assertEqual(1, g.get_weight('a', 'b'))
        self.assertEqual(1, g.get_weight('b', 'a'))
        self.assertEqual(5, g.get_weight('b', 'c'))
        self.assertEqual(5, g.get_weight('c', 'b'))
        self.assertEqual(1, g.get_weight('c', 'a'))
        self.assertEqual(1, g.get_weight('a', 'c'))

    def test_add_vertex(self):
        g = Graph()
        self.assertEqual({}, g.adj_list)

        g = Graph()
        g.add_vertex('a')
        self.assertEqual({'a': []}, g.adj_list)

        g = Graph()
        g.add_vertex('a')
        g.add_vertex('b')
        self.assertEqual({'a': [], 'b': []}, g.adj_list)

        g = Graph()
        g.add_vertex('a')
        g.add_vertex('b')
        g.add_vertex('c')
        self.assertEqual({'a': [], 'b': [], 'c': []}, g.adj_list)

    def test_add_edge(self):
        g = Graph()
        g.add_edge('a', 'b')
        self.assertEqual({'a': ['b'], 'b': ['a']}, g.adj_list)

        g = Graph()
        g.add_edge('a', 'b')
        g.add_edge('a', 'c')
        self.assertEqual({'a': ['b', 'c'], 'b': ['a'], 'c': ['a']}, g.adj_list)

        g = Graph()
        g.add_edge('a', 'b')
        g.add_edge('b', 'c')
        self.assertEqual({'a': ['b'], 'b': ['a', 'c'], 'c': ['b']}, g.adj_list)

        g = Graph()
        g.add_edge('a', 'b')
        g.add_edge('b', 'c')
        g.add_edge('c', 'a')
        self.assertEqual({'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'a']}, g.adj_list)

    def test_add_single_edge(self):
        self.assertEqual(True, True)

    def test_dfs(self):
        dg = Digraph()
        dg.add_edge('u', 'v')  # Cormen book example
        dg.add_edge('u', 'x')
        dg.add_edge('v', 'y')
        dg.add_edge('w', 'y')
        dg.add_edge('w', 'z')
        dg.add_edge('x', 'v')
        dg.add_edge('y', 'x')
        dg.add_edge('z', 'z')
        dfs(dg)

    def test_is_dag(self):
        dg = Digraph()

        dg.add_edge('a', 'b')
        self.assertEqual(True, is_directed_acyclic(dg))

        dg.add_edge('a', 'c')
        self.assertEqual(True, is_directed_acyclic(dg))

        dg.add_edge('a', 'd')
        self.assertEqual(True, is_directed_acyclic(dg))

        dg.add_edge('b', 'e')
        self.assertEqual(True, is_directed_acyclic(dg))

        dg.add_edge('b', 'f')
        self.assertEqual(True, is_directed_acyclic(dg))

        dg.add_edge('c', 'g')
        self.assertEqual(True, is_directed_acyclic(dg))

        dg = Digraph()
        dg.add_edge('a', 'a')
        self.assertEqual(False, is_directed_acyclic(dg))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'a')
        self.assertEqual(False, is_directed_acyclic(dg))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'a')
        self.assertEqual(False, is_directed_acyclic(dg))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'd')
        dg.add_edge('d', 'a')
        self.assertEqual(False, is_directed_acyclic(dg))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'd')
        dg.add_edge('d', 'b')
        self.assertEqual(False, is_directed_acyclic(dg))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'd')
        dg.add_edge('d', 'c')
        self.assertEqual(False, is_directed_acyclic(dg))

        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'd')
        dg.add_edge('d', 'd')
        self.assertEqual(False, is_directed_acyclic(dg))

        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'd')
        dg.add_edge('c', 'a')
        self.assertEqual(False, is_directed_acyclic(dg))

    def test_is_forest(self):
        g = Graph()

        g.add_vertex(0)
        self.assertEqual(True, is_forest(g))

        g.add_edge(0, 1)
        self.assertEqual(True, is_forest(g))

        g.add_edge(1, 2)
        self.assertEqual(True, is_forest(g))

        g.add_edge(2, 3)
        self.assertEqual(True, is_forest(g))

        g.add_edge(1, 4)
        self.assertEqual(True, is_forest(g))

        g.add_edge(2, 5)
        self.assertEqual(True, is_forest(g))

        g.add_edge(2, 6)
        self.assertEqual(True, is_forest(g))

        g.add_edge(7, 8)
        self.assertEqual(True, is_forest(g))

        g.add_edge(7, 9)
        self.assertEqual(True, is_forest(g))

        g.add_edge(7, 10)
        self.assertEqual(True, is_forest(g))

        g.add_edge(9, 11)
        self.assertEqual(True, is_forest(g))

        # g.add_edge(3, 5)
        # self.assertEqual(False, is_forest(g))

        # g.add_edge(8, 10)
        # self.assertEqual(False, is_forest(g))

        g.add_edge(1, 6)
        self.assertEqual(False, is_forest(g))

    def test_is_cyclic(self):
        dg = Digraph()

        dg.add_edge('a', 'b')
        self.assertEqual(False, is_directed_cyclic(dg))
        self.assertEqual(False, is_directed_cyclic_bfs(dg))

        dg.add_edge('a', 'c')
        self.assertEqual(False, is_directed_cyclic(dg))
        self.assertEqual(False, is_directed_cyclic_bfs(dg))

        dg.add_edge('a', 'd')
        self.assertEqual(False, is_directed_cyclic(dg))
        self.assertEqual(False, is_directed_cyclic_bfs(dg))

        dg.add_edge('b', 'e')
        self.assertEqual(False, is_directed_cyclic(dg))
        self.assertEqual(False, is_directed_cyclic_bfs(dg))

        dg.add_edge('b', 'f')
        self.assertEqual(False, is_directed_cyclic(dg))
        self.assertEqual(False, is_directed_cyclic_bfs(dg))

        dg.add_edge('c', 'g')
        self.assertEqual(False, is_directed_cyclic(dg))
        self.assertEqual(False, is_directed_cyclic_bfs(dg))

        dg = Digraph()
        dg.add_edge('a', 'a')
        self.assertEqual(True, is_directed_cyclic(dg))
        self.assertEqual(True, is_directed_cyclic_bfs(dg))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'a')
        self.assertEqual(True, is_directed_cyclic(dg))
        self.assertEqual(True, is_directed_cyclic_bfs(dg))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'a')
        self.assertEqual(True, is_directed_cyclic(dg))
        self.assertEqual(True, is_directed_cyclic_bfs(dg))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'd')
        dg.add_edge('d', 'a')
        self.assertEqual(True, is_directed_cyclic(dg))
        self.assertEqual(True, is_directed_cyclic_bfs(dg))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'd')
        dg.add_edge('d', 'b')
        self.assertEqual(True, is_directed_cyclic(dg))
        self.assertEqual(True, is_directed_cyclic_bfs(dg))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'd')
        dg.add_edge('d', 'c')
        self.assertEqual(True, is_directed_cyclic(dg))
        self.assertEqual(True, is_directed_cyclic_bfs(dg))

        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'd')
        dg.add_edge('d', 'd')
        self.assertEqual(True, is_directed_cyclic(dg))
        self.assertEqual(True, is_directed_cyclic_bfs(dg))

        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'd')
        dg.add_edge('c', 'a')
        self.assertEqual(True, is_directed_cyclic(dg))
        self.assertEqual(True, is_directed_cyclic_bfs(dg))

    def test_min_vertex_cover(self):
        # general graph in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        g.add_edge(2, 3)
        g.add_edge(2, 4)
        self.assertEqual(True, is_vertex_cover(g, [0, 1, 2]))
        self.assertEqual((0, 2, 1), min_vertex_cover_brute(g))

        # linear chain in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 6)
        g.add_edge(6, 7)
        # self.assertEqual(True, is_vertex_cover(g, [0, 2, 4, 6]))
        self.assertEqual((0, 2, 4, 6), min_vertex_cover_brute(g))

        # unweighted 2-approx killer in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 4)
        g.add_edge(1, 5)
        g.add_edge(2, 6)
        g.add_edge(3, 7)
        # self.assertEqual(True, is_vertex_cover(g, [0, 1, 2, 3]))
        self.assertEqual((0, 1, 2, 3), min_vertex_cover_brute(g))

        # weighted 2-approx killer in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(0, 4)
        # self.assertEqual(True, is_vertex_cover(g, [0, 1, 2, 3]))
        self.assertEqual((0,), min_vertex_cover_brute(g))

        # k5 in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(0, 4)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        g.add_edge(2, 3)
        g.add_edge(2, 4)
        g.add_edge(3, 4)
        # self.assertEqual(True, is_vertex_cover(g, [0, 1, 2, 3]))
        self.assertEqual((0, 1, 2, 3), min_vertex_cover_brute(g))

        # bipartite in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 3)
        g.add_edge(0, 4)
        g.add_edge(0, 5)
        g.add_edge(1, 5)
        g.add_edge(2, 5)
        # self.assertEqual(True, is_vertex_cover(g, [0, 5]))
        self.assertEqual((0, 5), min_vertex_cover_brute(g))

        # cs4234 sample in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(1, 4)
        g.add_edge(2, 3)
        g.add_edge(2, 5)
        g.add_edge(3, 6)
        g.add_edge(4, 5)
        g.add_edge(5, 6)
        g.add_edge(6, 7)
        # self.assertEqual(True, is_vertex_cover(g, [0, 2, 4, 6]))
        self.assertEqual((0, 2, 4, 6), min_vertex_cover_brute(g))

    def test_approx_vertex_cover(self):
        # general graph in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        g.add_edge(2, 3)
        g.add_edge(2, 4)
        self.assertEqual(True, is_vertex_cover(g, approx_vertex_cover(g)))

        # linear chain in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 6)
        g.add_edge(6, 7)
        self.assertEqual(True, is_vertex_cover(g, approx_vertex_cover(g)))

        # unweighted 2-approx killer in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 4)
        g.add_edge(1, 5)
        g.add_edge(2, 6)
        g.add_edge(3, 7)
        self.assertEqual(True, is_vertex_cover(g, approx_vertex_cover(g)))

        # weighted 2-approx killer in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(0, 4)
        self.assertEqual(True, is_vertex_cover(g, approx_vertex_cover(g)))

        # k5 in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 3)
        g.add_edge(0, 4)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        g.add_edge(2, 3)
        g.add_edge(2, 4)
        g.add_edge(3, 4)
        self.assertEqual(True, is_vertex_cover(g, approx_vertex_cover(g)))

        # bipartite in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 3)
        g.add_edge(0, 4)
        g.add_edge(0, 5)
        g.add_edge(1, 5)
        g.add_edge(2, 5)
        self.assertEqual(True, is_vertex_cover(g, approx_vertex_cover(g)))

        # cs4234 sample in https://visualgo.net/en/mvc
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(1, 4)
        g.add_edge(2, 3)
        g.add_edge(2, 5)
        g.add_edge(3, 6)
        g.add_edge(4, 5)
        g.add_edge(5, 6)
        g.add_edge(6, 7)
        self.assertEqual(True, is_vertex_cover(g, approx_vertex_cover(g)))

    def test_bipartite_check(self):
        # cp3 4.1 in https://visualgo.net/en/dfsbfs
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_vertex(5)
        g.add_edge(6, 7)
        g.add_edge(6, 8)
        self.assertEqual(False, is_bipartite_bfs(g))
        self.assertEqual(False, is_bipartite_dfs(g))

        # cp3 4.3 in https://visualgo.net/en/dfsbfs
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 4)
        g.add_edge(1, 2)
        g.add_edge(1, 5)
        g.add_edge(2, 3)
        g.add_edge(2, 6)
        g.add_edge(3, 7)
        g.add_edge(4, 8)
        g.add_edge(5, 6)
        g.add_edge(5, 10)
        g.add_edge(6, 11)
        g.add_edge(7, 12)
        g.add_edge(8, 9)
        g.add_edge(9, 10)
        g.add_edge(10, 11)
        g.add_edge(11, 12)
        self.assertEqual(False, is_bipartite_bfs(g))
        self.assertEqual(False, is_bipartite_dfs(g))

        # cp3 4.4 dag in https://visualgo.net/en/dfsbfs
        dg = Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(0, 2)
        dg.add_edge(1, 2)
        dg.add_edge(1, 3)
        dg.add_edge(2, 3)
        dg.add_edge(2, 5)
        dg.add_edge(3, 4)
        dg.add_edge(7, 6)
        self.assertEqual(False, is_bipartite_bfs(dg))
        self.assertEqual(False, is_bipartite_dfs(dg))

        # cp3 4.9 in https://visualgo.net/en/dfsbfs
        dg = Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(1, 3)
        dg.add_edge(2, 1)
        dg.add_edge(3, 2)
        dg.add_edge(3, 4)
        dg.add_edge(4, 5)
        dg.add_edge(5, 7)
        dg.add_edge(6, 4)
        dg.add_edge(7, 6)
        self.assertEqual(False, is_bipartite_bfs(dg))
        self.assertEqual(False, is_bipartite_dfs(dg))

        # cp3 4.17 dag in https://visualgo.net/en/dfsbfs
        dg = Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(0, 2)
        dg.add_edge(0, 3)
        dg.add_edge(1, 3)
        dg.add_edge(1, 4)
        dg.add_edge(2, 4)
        dg.add_edge(3, 4)
        self.assertEqual(False, is_bipartite_bfs(dg))
        self.assertEqual(False, is_bipartite_dfs(dg))

        # cp3 4.18 dag bipartite in https://visualgo.net/en/dfsbfs
        dg = Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(0, 2)
        dg.add_edge(1, 3)
        dg.add_edge(2, 3)
        dg.add_edge(3, 4)
        self.assertEqual(True, is_bipartite_bfs(dg))
        self.assertEqual(True, is_bipartite_dfs(dg))

        # cp3 4.19 bipartite in https://visualgo.net/en/dfsbfs
        dg = Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(0, 4)
        dg.add_edge(1, 2)
        dg.add_edge(2, 1)
        dg.add_edge(2, 3)
        self.assertEqual(True, is_bipartite_bfs(dg))
        self.assertEqual(True, is_bipartite_dfs(dg))

    def test_articulation_points(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        self.assertEqual([1], articulation_point(g))
