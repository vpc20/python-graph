from itertools import combinations, permutations
from random import randrange

from Graph import Graph, Digraph


def random_graph(n, p, directed=False):
    """
    Create a random graph

    :param n: number of nodes
    :param p: probability of edge creation (0 to 100)
    :param directed: set to True to generate a directed graph. Default is False (undirected graph)
    :return: graph
    """
    if not directed:
        g = Graph()
        for i in range(n):
            g.add_vertex(i)
        for u, v in combinations(g.vertices, 2):
            # print(u, v)
            if randrange(1, 101) <= p:
                g.add_edge(u, v)
        return g
    else:
        dg = Digraph()
        for i in range(n):
            dg.add_vertex(i)
        for u, v in permutations(dg.vertices, 2):
            # print(u, v)
            if randrange(1, 101) <= p:
                dg.add_edge(u, v)
        return dg


if __name__ == '__main__':
    g = random_graph(10, 10)
    print(g.vertices)
    print(g.edges)

    dg = random_graph(4, 50, directed=True)
    print(dg.vertices)
    print(dg.edges)
