import sys
from math import inf
from random import randint
from unittest import TestCase
import networkx as nx
import Graph as gx
from FloydWarshall import floyd_warshall


class Test(TestCase):
    def test_floyd_warshall(self):
        for _ in range(1000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
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

            n = nxg.number_of_nodes()  # convert adj list to adj matrix
            wts = [[0 if i == j else sys.maxsize for j in range(n)] for i in range(n)]
            for u, v in nxg.edges:
                wts[u][v] = nxg[u][v]['weight']
            # print(wts)
            pred1, dist1 = nx.floyd_warshall_predecessor_and_distance(nxg)
            pred2, dist2 = floyd_warshall(wts)
            print(dist1)
            print(dist2)

            dist1x = [[0 for j in range(n)] for i in range(n)]
            for k, v in dist1.items():
                for k1, v1 in v.items():
                    if v1 == inf:
                        dist1x[k][k1] = sys.maxsize
                    else:
                        dist1x[k][k1] = v1
            print(dist1x)

            self.assertEqual(dist1x, dist2)
