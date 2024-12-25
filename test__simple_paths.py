from random import randint, choice
from unittest import TestCase
import networkx as nx
import Graph as gx
from SimplePaths import all_simple_paths_dfs, all_simple_paths_bfs


class Test(TestCase):
    def test_all_simple_paths_dfs(self):
        for _ in range(1000):
            nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Digraph()
            g.add_vertices_from(nxg.nodes)
            g.add_edges_from(nxg.edges)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            if nxg.number_of_nodes() >= 2:
                s = choice(list(nxg.nodes))
                while True:
                    t = choice(list(nxg.nodes))
                    if t != s:
                        break
                # print([path for path in nx.all_simple_paths(nxg, s, t)])
                # print(all_simple_paths_dfs(g, s, t))
                self.assertEqual([path for path in nx.all_simple_paths(nxg, s, t)], all_simple_paths_dfs(g, s, t))

    def test_all_simple_paths_bfs(self):
        for _ in range(1000):
            while True:
                nxg = nx.fast_gnp_random_graph(randint(1, 10), randint(1, 9) / 10, directed=True)
                # nxg = nx.fast_gnp_random_graph(randint(6, 7), randint(7, 9) / 10, directed=True)
                if nx.is_directed_acyclic_graph(nxg):
                    break
            print('***')
            print(sorted(nxg.nodes))
            print(sorted(nxg.edges))

            g = gx.Digraph()
            g.add_vertices_from(nxg.nodes)
            g.add_edges_from(nxg.edges)
            print(sorted(g.vertices))
            print(sorted(g.edges))

            if nxg.number_of_nodes() >= 2:
                s = choice(list(nxg.nodes))
                while True:
                    t = choice(list(nxg.nodes))
                    if t != s:
                        break
                print(s)
                print(t)
                print([path for path in nx.all_simple_paths(nxg, s, t)])
                print(all_simple_paths_bfs(g, s, t))
                self.assertEqual(sorted(path for path in nx.all_simple_paths(nxg, s, t)),
                                 sorted(all_simple_paths_bfs(g, s, t)))
