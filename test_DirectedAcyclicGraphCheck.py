from random import randint
from unittest import TestCase
import networkx as nx
import Graph as gx
from DirectedAcyclicGraphCheck import is_directed_acyclic_graph, is_directed_acyclic_dfs, is_directed_acyclic_bfs


class Test(TestCase):
    def test_is_directed_acyclic_graph(self):
        for _ in range(1000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            # nxg = nx.fast_gnp_random_graph(randint(1, 3),5 / 10, directed=True)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Digraph()
            for node in nxg.nodes:
                g.add_vertex(node)
            for u, v in nxg.edges:
                g.add_edge(u, v)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            print(nx.is_directed_acyclic_graph(nxg))
            assert nx.is_directed_acyclic_graph(nxg) == is_directed_acyclic_graph(g)
            assert nx.is_directed_acyclic_graph(nxg) == is_directed_acyclic_dfs(g)
            # assert nx.is_directed_acyclic_graph(nxg) == is_directed_acyclic_dfs_iter(g)
            assert nx.is_directed_acyclic_graph(nxg) == is_directed_acyclic_bfs(g)
