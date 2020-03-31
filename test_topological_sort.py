from unittest import TestCase

from Graph import Digraph
from TopologicalSort import topological_sort, topological_sort_dfs


class TestTopologicalSort(TestCase):
    def test_topological_sort(self):
        # cp3 4.4 dag in https://visualgo.net/en/dfsbfs
        dg = Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(0, 2)
        dg.add_edge(1, 2)
        dg.add_edge(1, 3)
        dg.add_edge(2, 3)
        dg.add_edge(2, 5)
        dg.add_edge(3, 4)
        dg.add_edge(7, 6)
        # print(topological_sort(dg))
        self.assertEqual([0, 7, 1, 6, 2, 3, 5, 4], topological_sort(dg))
        self.assertEqual([7, 6, 0, 1, 2, 5, 3, 4], topological_sort_dfs(dg))

        # cp3 4.17 dag in https://visualgo.net/en/dfsbfs
        dg = Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(0, 2)
        dg.add_edge(0, 3)
        dg.add_edge(1, 3)
        dg.add_edge(1, 4)
        dg.add_edge(2, 4)
        dg.add_edge(3, 4)
        self.assertEqual([0, 1, 2, 3, 4], topological_sort(dg))
        self.assertEqual([0, 2, 1, 3, 4], topological_sort_dfs(dg))

        # cp3 4.18 dag bipartite in https://visualgo.net/en/dfsbfs
        dg = Digraph()
        dg.add_edge(0, 1)
        dg.add_edge(0, 2)
        dg.add_edge(1, 3)
        dg.add_edge(2, 3)
        dg.add_edge(3, 4)
        self.assertEqual([0, 1, 2, 3, 4], topological_sort(dg))
        self.assertEqual([0, 2, 1, 3, 4], topological_sort_dfs(dg))

