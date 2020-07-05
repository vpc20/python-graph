from unittest import TestCase

from Graph import Digraph
from TopologicalSort import topological_sort


class TestTopologicalSort(TestCase):
    def test_topological_sort(self):
        # cp3 4.4 dag in https://visualgo.net/en/dfsbfs
        dg = Digraph()
        dg.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 5), (3, 4), (7, 6)])
        self.assertEqual([7, 6, 0, 1, 2, 5, 3, 4], list(topological_sort(dg)))

        # cp3 4.17 dag in https://visualgo.net/en/dfsbfs
        dg = Digraph()
        dg.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (3, 4)])
        self.assertEqual([0, 2, 1, 3, 4], list(topological_sort(dg)))

        # cp3 4.18 dag bipartite in https://visualgo.net/en/dfsbfs
        dg = Digraph()
        dg.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)])
        self.assertEqual([0, 2, 1, 3, 4], list(topological_sort(dg)))
