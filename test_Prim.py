from random import randint
from unittest import TestCase
import networkx as nx
import Graph as gx
from Prim import mst_prim


class Test(TestCase):
    def test_mst_prim(self):
        for _ in range(10000):
            while True:
                nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=False)
                if nx.is_connected(nxg):
                    break
            for u, v in nxg.edges:
                nxg[u][v]['weight'] = randint(1, 12)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Graph()
            g.add_vertices_from(nxg.nodes)
            for u, v in nxg.edges:
                g.add_edge(u, v, nxg[u][v]['weight'])
            print(sorted(g.vertices))
            print(sorted(g.edges))

            w1 = sum([nxg[u][v]['weight'] for u, v in nx.minimum_spanning_tree(nxg).edges])
            w2 = sum([g.weight(u, v) for u, v in mst_prim(g).edges])
            self.assertEqual(w1, w2)
