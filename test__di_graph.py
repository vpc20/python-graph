from random import randint, choice
from unittest import TestCase
import Graph as gx
import networkx as nx


class TestGraph(TestCase):
    def test_add_edge(self):
        for _ in range(1000):
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

            assert sorted(nxg.nodes) == sorted(g.vertices)
            assert sorted(nxg.edges) == sorted(g.edges)

    def test_add_edges_from(self):
        for _ in range(1000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Digraph()
            for node in nxg.nodes:
                g.add_vertex(node)
            g.add_edges_from(nxg.edges)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            assert sorted(nxg.nodes) == sorted(g.vertices)
            assert sorted(nxg.edges) == sorted(g.edges)

    def test_add_weighted_edges_from(self):
        for _ in range(1000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))
            elist = []
            for u, v in nxg.edges:
                nxg[u][v]['weight'] = randint(1, 20)
                elist.append((u, v, nxg[u][v]['weight']))

            g = gx.Digraph()
            for node in nxg.nodes:
                g.add_vertex(node)
            g.add_weighted_edges_from(elist)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            assert sorted(nxg.nodes) == sorted(g.vertices)
            assert sorted(nxg.edges) == sorted(g.edges)
            x = sum([nxg[u][v]['weight'] for u, v in nxg.edges])
            y = sum([g.weight(u, v) for u, v in g.edges])
            assert x == y

    def test_remove_edge(self):
        for _ in range(1000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Digraph()
            for node in nxg.nodes:
                g.add_vertex(node)
            g.add_edges_from(nxg.edges)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            if g.edges:
                u, v = choice(g.edges)  # random choice
                g.remove_edge(u, v)
                nxg.remove_edge(u, v)

            assert sorted(nxg.nodes) == sorted(g.vertices)
            assert sorted(nxg.edges) == sorted(g.edges)

        for _ in range(1000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Digraph()
            for node in nxg.nodes:
                g.add_vertex(node)
            g.add_edges_from(nxg.edges)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            for u, v in g.edges:
                g.remove_edge(u, v)
                nxg.remove_edge(u, v)
                assert sorted(nxg.nodes) == sorted(g.vertices)
                assert sorted(nxg.edges) == sorted(g.edges)

    def test_remove_vertex(self):
        for _ in range(1000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Digraph()
            for node in nxg.nodes:
                g.add_vertex(node)
            g.add_edges_from(nxg.edges)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            v = choice(g.vertices)  # random choice
            g.remove_vertex(v)
            nxg.remove_node(v)

            assert sorted(nxg.nodes) == sorted(g.vertices)
            assert sorted(nxg.edges) == sorted(g.edges)

        for _ in range(1000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Digraph()
            for node in nxg.nodes:
                g.add_vertex(node)
            g.add_edges_from(nxg.edges)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            for v in g.vertices:
                g.remove_vertex(v)
                nxg.remove_node(v)
                assert sorted(nxg.nodes) == sorted(g.vertices)
                assert sorted(nxg.edges) == sorted(g.edges)
