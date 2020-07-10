import sys
from unittest import TestCase
from random import randint
import networkx as nx
import Graph as gx
from Dijkstra import dijkstra


class Test(TestCase):
    def test_dijkstra(self):
        for _ in range(10000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))
            src = 0

            g = gx.Digraph()
            g.add_vertices_from(nxg.nodes)
            g.add_edges_from(nxg.edges)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            pred1, dist1 = nx.dijkstra_predecessor_and_distance(nxg, src)
            print(pred1)
            print(dist1)
            pred2, dist2 = dijkstra(g, src)
            print(pred2)
            print(dist2)
            self.assertEqual(dist1, {k: v for k, v in dist2.items() if v != sys.maxsize})
