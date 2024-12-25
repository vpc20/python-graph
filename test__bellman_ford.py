import sys
from random import randint
from unittest import TestCase
import networkx as nx
import Graph as gx
from BellmanFord import bellman_ford


class Test(TestCase):
    def test_bellman_ford(self):
        for _ in range(1000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            for u, v in nxg.edges:
                nxg[u][v]['weight'] = randint(1, 12)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Digraph()
            g.add_vertices_from(nxg.nodes)
            for u, v in nxg.edges:
                g.add_edge(u, v, nxg[u][v]['weight'])
            print(sorted(g.vertices))
            print(sorted(g.edges))

            pred1, dist1 = nx.bellman_ford_predecessor_and_distance(nxg, 0)
            print(pred1)
            print(dist1)
            pred2, dist2 = bellman_ford(g, 0)
            print(pred2)
            print(dist2)
            self.assertEqual(dist1, {k: v for k, v in dist2.items() if v != sys.maxsize})
