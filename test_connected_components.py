from random import randint
from unittest import TestCase

import networkx as nx

import Graph as gx
from ConnectedComponents import connected_components, connected_components_bfs, connected_components_dj, is_connected, \
    is_connected_bfs, strongly_connected_components


class TestConnectedComponents(TestCase):
    def test_is_connected(self):
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

            self.assertEqual(nx.is_connected(nxg), is_connected(g))
            self.assertEqual(nx.is_connected(nxg), is_connected_bfs(g))

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

    def test_strongly_connected_components(self):
        for _ in range(10000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Digraph()
            for node in nxg.nodes:
                g.add_vertex(node)
            for u, v in nxg.edges:
                g.add_edge(u, v)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            x = sorted(sorted(list(e)) for e in nx.strongly_connected_components(nxg))
            print(x)
            y = sorted(sorted(e) for e in strongly_connected_components(g))
            print(y)
            self.assertEqual(x, y)

    def test1_strongly_connected_components(self):
        # cp3 4.4 dag in https://visualgo.net/en/dfsbfs
        dg = gx.Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(0, 2)
        dg.add_edge(1, 2)
        dg.add_edge(1, 3)
        dg.add_edge(2, 3)
        dg.add_edge(2, 5)
        dg.add_edge(3, 4)
        dg.add_edge(7, 6)
        # print(strongly_connected_components(dg))
        self.assertEqual([[7], [6], [0], [1], [2], [5], [3], [4]], strongly_connected_components(dg))

        # cp3 4.9 in https://visualgo.net/en/dfsbfs
        dg = gx.Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(1, 3)
        dg.add_edge(2, 1)
        dg.add_edge(3, 2)
        dg.add_edge(3, 4)
        dg.add_edge(4, 5)
        dg.add_edge(5, 7)
        dg.add_edge(6, 4)
        dg.add_edge(7, 6)
        print(strongly_connected_components(dg))
        self.assertEqual([[0], [1, 2, 3], [4, 5, 6, 7]],
                         sorted(sorted(e) for e in strongly_connected_components(dg)))

        # cp3 4.17 dag in https://visualgo.net/en/dfsbfs
        dg = gx.Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(0, 2)
        dg.add_edge(0, 3)
        dg.add_edge(1, 3)
        dg.add_edge(1, 4)
        dg.add_edge(2, 4)
        dg.add_edge(3, 4)
        # print(strongly_connected_components(dg))
        self.assertEqual([[0], [2], [1], [3], [4]], strongly_connected_components(dg))

        # cp3 4.18 dag bipartite in https://visualgo.net/en/dfsbfs
        dg = gx.Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(0, 2)
        dg.add_edge(1, 3)
        dg.add_edge(2, 3)
        dg.add_edge(3, 4)
        print(strongly_connected_components(dg))
        self.assertEqual([[0], [2], [1], [3], [4]], strongly_connected_components(dg))

        # cp3 4.19 bipartite in https://visualgo.net/en/dfsbfs
        dg = gx.Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(0, 4)
        dg.add_edge(1, 2)
        dg.add_edge(2, 1)
        dg.add_edge(2, 3)
        print(strongly_connected_components(dg))
        self.assertEqual([[0], [4], [1, 2], [3]], strongly_connected_components(dg))
