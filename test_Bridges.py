from random import randint
from unittest import TestCase

import networkx as nx

import Graph as gx
from Bridges import bridges


class Test(TestCase):
    def test_bridges(self):
        for _ in range(1000):
            while True:
                nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=False)
                if nx.is_connected(nxg):
                    break
            # for u, v in nxg.edges:
            #     nxg[u][v]['weight'] = randint(1, 12)
            # print(sorted(nxg.nodes))
            # print(sorted(nxg.edges))

            g = gx.Graph()
            g.add_vertices_from(nxg.nodes)
            # for u, v in nxg.edges:
            #     g.add_edge(u, v, nxg[u][v]['weight'])
            for u, v in nxg.edges:
                g.add_edge(u, v)
            # print(sorted(g.vertices))
            # print(sorted(g.edges))

            x = [(u, v) if u < v else (v, u) for u, v in list(nx.bridges(nxg))]
            y = [(u, v) if u < v else (v, u) for u, v in bridges(g)]
            if x and y:
                print(sorted(x))
                print(sorted(y))
            self.assertEqual(sorted(x), sorted(y))
