from random import randint
from unittest import TestCase
import networkx as nx
import Graph as gx
from DfsTree import dfs_tree


class Test(TestCase):
    def test_dfs_tree(self):
        for _ in range(10000):
            print('')
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))
            src = 0

            g = gx.Digraph()
            for node in nxg.nodes:
                g.add_vertex(node)
            g.add_edges_from(nxg.edges)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            t1 = nx.dfs_tree(nxg, src)
            t2 = dfs_tree(g, src)
            print(t1.nodes)
            print(t2.vertices)

            self.assertEqual(sorted(t1.nodes), sorted(t2.vertices))
            self.assertEqual(sorted(t1.edges), sorted(t2.edges))
            # self.assertEqual(sorted([sorted(e) for e in t1.edges]), sorted([sorted(e) for e in t2.edges]))
