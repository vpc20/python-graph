from random import randint
from unittest import TestCase
import networkx as nx
import Graph as gx
from UndirectedAcyclicGraphCheck import is_undirected_acyclic_dfs, is_undirected_acyclic_bfs


class Test(TestCase):
    def test_is_undirected_acyclic(self):
        for _ in range(10000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=False)
            # nxg = nx.fast_gnp_random_graph(randint(1, 5), randint(1, 9) / 10, directed=False)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Graph()
            g.add_vertices_from(nxg.nodes)
            g.add_edges_from(nxg.edges)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            # print(nx.find_cycle(nxg))
            try:
                print(nx.find_cycle(nxg))
                x = False
            except nx.NetworkXNoCycle:
                x = True
            self.assertEqual(x, is_undirected_acyclic_dfs(g))
            self.assertEqual(x, is_undirected_acyclic_bfs(g))
