from unittest import TestCase

from Dijkstra import dijkstra_sssp
from Graph import Digraph


class TestDijkstraSssp(TestCase):
    def test_dijkstra_sssp(self):
        dg = Digraph()
        dg.add_vertex('a')
        self.assertEqual([], dijkstra_sssp(dg, 'a'))

        dg = Digraph()
        dg.add_edge('a', 'b')
        self.assertEqual([(1, ['a', 'b'])], dijkstra_sssp(dg, 'a'))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        self.assertEqual([(1, ['a', 'b']), (2, ['a', 'b', 'c'])],
                         dijkstra_sssp(dg, 'a'))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('a', 'c')
        self.assertEqual([(1, ['a', 'b']), (1, ['a', 'c'])],
                         dijkstra_sssp(dg, 'a'))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'a')
        print(dg)
        self.assertEqual([(1, ['a', 'b']), (2, ['a', 'b', 'c'])],
                         dijkstra_sssp(dg, 'a'))

        dg = Digraph()
        dg.add_edge('a', 'b')
        dg.add_edge('b', 'c')
        dg.add_edge('c', 'a')
        dg.add_edge('c', 'd')
        print(dg)
        self.assertEqual([(1, ['a', 'b']), (2, ['a', 'b', 'c']), (3, ['a', 'b', 'c', 'd'])],
                         dijkstra_sssp(dg, 'a'))
