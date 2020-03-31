from unittest import TestCase

from Graph import Graph, is_spanning_tree, gen_all_graphs, is_connected
from Kruskal import mst_kruskal
from MstBrute import mst_brute
from Prim import mst_prim


class TestMst(TestCase):
    def test_mst(self):
        g = Graph()

        # cp 4.10 in https://visualgo.net/en/mst
        g.adj_list = {0: [1, 4, 3, 2], 1: [0, 2], 4: [0, 3], 3: [0, 2, 4], 2: [0, 1, 3]}
        g.weights = {(0, 1): 4, (1, 0): 4, (1, 2): 2, (2, 1): 2, (2, 3): 8, (3, 2): 8, (3, 4): 9, (4, 3): 9, (0, 4): 6,
                     (4, 0): 6, (0, 3): 6, (3, 0): 6, (0, 2): 4, (2, 0): 4}
        w1, edges1 = mst_kruskal(g)
        w2, edges2 = mst_prim(g)
        self.assertEqual(w1, w2)
        self.assertEqual(sorted([sorted([v1, v2]) for v1, v2 in edges1]),
                         sorted([sorted([v1, v2]) for v1, v2 in edges2]))
        self.assertEqual(True, is_spanning_tree(g, edges1))
        self.assertEqual(True, is_spanning_tree(g, edges2))

        # cp 4.14 in https://visualgo.net/en/mst
        g.adj_list = {0: [2, 1], 2: [0, 3, 1], 1: [0, 2, 4, 3], 3: [2, 1, 4], 4: [1, 3]}
        g.weights = {(0, 2): 75, (2, 0): 75, (2, 3): 51, (3, 2): 51, (2, 1): 95, (1, 2): 95, (1, 4): 42, (4, 1): 42,
                     (0, 1): 9, (1, 0): 9, (1, 3): 19, (3, 1): 19, (3, 4): 31, (4, 3): 31}
        w1, edges1 = mst_kruskal(g)
        w2, edges2 = mst_prim(g)
        self.assertEqual(w1, w2)
        self.assertEqual(sorted([sorted([v1, v2]) for v1, v2 in edges1]),
                         sorted([sorted([v1, v2]) for v1, v2 in edges2]))
        self.assertEqual(True, is_spanning_tree(g, edges1))
        self.assertEqual(True, is_spanning_tree(g, edges2))

        # k5 in https://visualgo.net/en/mst
        g.adj_list = {0: [1, 3, 2, 4], 1: [0, 2, 4, 3], 3: [0, 2, 4, 1], 2: [1, 3, 0, 4], 4: [1, 3, 0, 2]}
        g.weights = {(0, 1): 24, (1, 0): 24, (1, 2): 22, (2, 1): 22, (2, 3): 19, (3, 2): 19, (3, 4): 19, (4, 3): 19,
                     (4, 0): 22, (0, 4): 22, (0, 3): 13, (3, 0): 13, (3, 1): 13, (1, 3): 13, (1, 4): 13, (4, 1): 13,
                     (4, 2): 14, (2, 4): 14, (2, 0): 13, (0, 2): 13}
        w1, edges1 = mst_kruskal(g)
        w2, edges2 = mst_prim(g)
        self.assertEqual(w1, w2)
        self.assertEqual(sorted([sorted([v1, v2]) for v1, v2 in edges1]),
                         sorted([sorted([v1, v2]) for v1, v2 in edges2]))
        self.assertEqual(True, is_spanning_tree(g, edges1))
        self.assertEqual(True, is_spanning_tree(g, edges2))

        # rail in https://visualgo.net/en/mst
        g.adj_list = {0: [1], 1: [0, 2, 6, 7], 2: [1, 3, 7, 8], 6: [1, 5, 7], 7: [1, 2, 6, 8], 3: [2, 4, 8],
                      8: [2, 3, 7, 9], 4: [3], 5: [6], 9: [8]}
        g.weights = {(0, 1): 10, (1, 0): 10, (1, 2): 10, (2, 1): 10, (2, 3): 10, (3, 2): 10, (3, 4): 10, (4, 3): 10,
                     (5, 6): 10, (6, 5): 10, (6, 7): 10, (7, 6): 10, (7, 8): 10, (8, 7): 10, (8, 9): 10, (9, 8): 10,
                     (1, 6): 8, (6, 1): 8, (1, 7): 13, (7, 1): 13, (2, 7): 8, (7, 2): 8, (2, 8): 13, (8, 2): 13,
                     (3, 8): 8,
                     (8, 3): 8}
        w1, edges1 = mst_kruskal(g)
        w2, edges2 = mst_prim(g)
        self.assertEqual(w1, w2)
        self.assertEqual(sorted([sorted([v1, v2]) for v1, v2 in edges1]),
                         sorted([sorted([v1, v2]) for v1, v2 in edges2]))
        self.assertEqual(True, is_spanning_tree(g, edges1))
        self.assertEqual(True, is_spanning_tree(g, edges2))

        # tessellation in https://visualgo.net/en/mst
        g.adj_list = {0: [1, 2], 1: [0, 2, 4, 3], 2: [0, 1, 3, 6], 4: [1, 3, 5], 3: [1, 2, 4, 6, 8, 7, 5], 6: [2, 3, 8],
                      5: [4, 3, 7], 8: [3, 6, 7], 7: [3, 8, 5]}
        g.weights = {(0, 1): 8, (1, 0): 8, (0, 2): 12, (2, 0): 12, (1, 2): 13, (2, 1): 13, (1, 4): 9, (4, 1): 9,
                     (2, 3): 14,
                     (3, 2): 14, (1, 3): 25, (3, 1): 25, (4, 3): 20, (3, 4): 20, (2, 6): 21, (6, 2): 21, (3, 6): 12,
                     (6, 3): 12, (6, 8): 11, (8, 6): 11, (3, 8): 16, (8, 3): 16, (3, 7): 12, (7, 3): 12, (7, 8): 9,
                     (8, 7): 9, (4, 5): 19, (5, 4): 19, (5, 7): 11, (7, 5): 11, (3, 5): 8, (5, 3): 8}
        w1, edges1 = mst_kruskal(g)
        w2, edges2 = mst_prim(g)
        self.assertEqual(w1, w2)
        self.assertEqual(sorted([sorted([v1, v2]) for v1, v2 in edges1]),
                         sorted([sorted([v1, v2]) for v1, v2 in edges2]))
        self.assertEqual(True, is_spanning_tree(g, edges1))
        self.assertEqual(True, is_spanning_tree(g, edges2))

        for g in gen_all_graphs(4):
            if is_connected(g):
                print(g)
                w1, edges1 = mst_kruskal(g)
                w2, edges2 = mst_prim(g)
                w3, edges3 = mst_brute(g)
                self.assertEqual(w1, w2)
                self.assertEqual(w1, w3)
                # self.assertEqual(sorted([sorted([v1, v2]) for v1, v2 in edges1]),
                #                  sorted([sorted([v1, v2]) for v1, v2 in edges2]))
                # self.assertEqual(True, is_spanning_tree(g, edges1))
                # self.assertEqual(True, is_spanning_tree(g, edges2))

