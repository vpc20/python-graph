from random import randint
from unittest import TestCase

import networkx as nx

import Graph as gx
from ConnectedComponents import connected_components, connected_components_bfs, connected_components_dj


class TestConnectedComponents(TestCase):
    def test_connected_components(self):
        for _ in range(10000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Graph()
            for node in nxg.nodes:
                g.add_vertex(node)
            for u, v in nxg.edges:
                g.add_edge(u, v)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            # print(sorted([sorted(list(e)) for e in nx.connected_components(nxg)]))
            # print(sorted([sorted(e) for e in connected_components_bfs(g)]))
            self.assertEqual(sorted([sorted(list(e)) for e in nx.connected_components(nxg)]),
                             sorted([sorted(e) for e in connected_components(g)]))
            self.assertEqual(sorted([sorted(list(e)) for e in nx.connected_components(nxg)]),
                             sorted([sorted(e) for e in connected_components_bfs(g)]))
            self.assertEqual([e for e in nx.connected_components(nxg)],
                             connected_components_dj(g))
            # print([e for e in nx.connected_components(nxg)])
            # print(connected_components_dj(g))

            # def test_strongly_connected_components(self):
            #     # cp3 4.1 in https://visualgo.net/en/dfsbfs
            #     g = Graph()
            #     g.add_edge(0, 1)
            #     g.add_edge(1, 2)
            #     g.add_edge(1, 3)
            #     g.add_edge(2, 3)
            #     g.add_edge(3, 4)
            #     g.add_vertex(5)
            #     g.add_edge(6, 7)
            #     g.add_edge(6, 8)
            #     self.assertEqual([{6, 7, 8}, {5}, {0, 1, 2, 3, 4}], strongly_connected_components(g))
            #
            #     # cp3 4.3 in https://visualgo.net/en/dfsbfs
            #     g = Graph()
            #     g.add_edge(0, 1)
            #     g.add_edge(0, 4)
            #     g.add_edge(1, 2)
            #     g.add_edge(1, 5)
            #     g.add_edge(2, 3)
            #     g.add_edge(2, 6)
            #     g.add_edge(3, 7)
            #     g.add_edge(4, 8)
            #     g.add_edge(5, 6)
            #     g.add_edge(5, 10)
            #     g.add_edge(6, 11)
            #     g.add_edge(7, 12)
            #     g.add_edge(8, 9)
            #     g.add_edge(9, 10)
            #     g.add_edge(10, 11)
            #     g.add_edge(11, 12)
            #     # print(strongly_connected_components(g))
            #     self.assertEqual([{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}], strongly_connected_components(g))
            #
            #     # cp3 4.4 dag in https://visualgo.net/en/dfsbfs
            #     dg = Digraph()
            #     dg.add_edge(0, 1)
            #     dg.add_edge(0, 2)
            #     dg.add_edge(1, 2)
            #     dg.add_edge(1, 3)
            #     dg.add_edge(2, 3)
            #     dg.add_edge(2, 5)
            #     dg.add_edge(3, 4)
            #     dg.add_edge(7, 6)
            #     # print(strongly_connected_components(dg))
            #     self.assertEqual([{7}, {6}, {0}, {1}, {2}, {5}, {3}, {4}], strongly_connected_components(dg))
            #
            #     # cp3 4.9 in https://visualgo.net/en/dfsbfs
            #     dg = Digraph()
            #     dg.add_edge(0, 1)
            #     dg.add_edge(1, 3)
            #     dg.add_edge(2, 1)
            #     dg.add_edge(3, 2)
            #     dg.add_edge(3, 4)
            #     dg.add_edge(4, 5)
            #     dg.add_edge(5, 7)
            #     dg.add_edge(6, 4)
            #     dg.add_edge(7, 6)
            #     # print(strongly_connected_components(dg))
            #     self.assertEqual([{0}, {1, 2, 3}, {4, 5, 6, 7}], strongly_connected_components(dg))
            #
            #     # cp3 4.17 dag in https://visualgo.net/en/dfsbfs
            #     dg = Digraph()
            #     dg.add_edge(0, 1)
            #     dg.add_edge(0, 2)
            #     dg.add_edge(0, 3)
            #     dg.add_edge(1, 3)
            #     dg.add_edge(1, 4)
            #     dg.add_edge(2, 4)
            #     dg.add_edge(3, 4)
            #     # print(strongly_connected_components(dg))
            #     self.assertEqual([{0}, {2}, {1}, {3}, {4}], strongly_connected_components(dg))
            #
            #     # cp3 4.18 dag bipartite in https://visualgo.net/en/dfsbfs
            #     dg = Digraph()
            #     dg.add_edge(0, 1)
            #     dg.add_edge(0, 2)
            #     dg.add_edge(1, 3)
            #     dg.add_edge(2, 3)
            #     dg.add_edge(3, 4)
            #     print(strongly_connected_components(dg))
            #     self.assertEqual([{0}, {2}, {1}, {3}, {4}], strongly_connected_components(dg))
            #
            #     # cp3 4.19 bipartite in https://visualgo.net/en/dfsbfs
            #     dg = Digraph()
            #     dg.add_edge(0, 1)
            #     dg.add_edge(0, 4)
            #     dg.add_edge(1, 2)
            #     dg.add_edge(2, 1)
            #     dg.add_edge(2, 3)
            #     print(strongly_connected_components(dg))
            #     self.assertEqual([{0}, {4}, {1, 2}, {3}], strongly_connected_components(dg))
