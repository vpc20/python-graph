from random import randint
from unittest import TestCase
import networkx as nx
import Graph as gx
from directed_acyclic_graph_check import is_directed_acyclic_graph, is_directed_acyclic_dfs, is_directed_acyclic_bfs, \
    is_directed_acyclic_dfs_iter, is_directed_acyclic_bfs2


class Test(TestCase):
    def test_is_directed_acyclic_graph(self):
        for _ in range(100000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            # nxg = nx.fast_gnp_random_graph(randint(1, 3),5 / 10, directed=True)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Digraph()
            g.add_vertices_from(nxg.nodes)
            g.add_edges_from(nxg.edges)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            print(nx.is_directed_acyclic_graph(nxg))
            # self.assertEqual(nx.is_directed_acyclic_graph(nxg), is_directed_acyclic_graph(g))

            assert nx.is_directed_acyclic_graph(nxg) == is_directed_acyclic_graph(g)
            assert nx.is_directed_acyclic_graph(nxg) == is_directed_acyclic_dfs(g)
            assert nx.is_directed_acyclic_graph(nxg) == is_directed_acyclic_bfs(g)
            assert nx.is_directed_acyclic_graph(nxg) == is_directed_acyclic_bfs2(g)

            # assert nx.is_directed_acyclic_graph(nxg) == is_directed_acyclic_dfs_iter(g)
            # self.assertEqual(nx.is_directed_acyclic_graph(nxg), is_directed_acyclic_bfs2(g))
