# The traveling-salesman problem
# In the traveling-salesman problem introduced in Section 34.5.4, we are given a
# complete undirected graph G = (V, E)  that has a nonnegative integer cost c(u,v)
# associated with each edge (u,v) ϵ E, and we must find a hamiltonian cycle
# (a tour) of G with minimum cost.
from Graph import Graph, complete_graph
from Dfs import dfs_vertices
from Kruskal import mst_kruskal


def approx_tsp_tour(g):
    _, kruskal_edges = mst_kruskal(g)
    mst = Graph()
    mst.add_edges_from(kruskal_edges)
    dfs_vert_arr = dfs_vertices(g)  # preorder tree walk
    return dfs_vert_arr


if __name__ == '__main__':
    g = complete_graph(8, alpha=True)
    print(g)
    print(g.weights)

    g = Graph()
    g.adj_list = {'a': ['b', 'c', 'h', 'd', 'e', 'f', 'g'], 'b': ['a', 'c', 'd', 'e', 'f', 'g', 'h'],
                  'c': ['a', 'b', 'h', 'd', 'e', 'f', 'g'], 'h': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                  'd': ['a', 'b', 'c', 'e', 'f', 'g', 'h'], 'e': ['a', 'b', 'c', 'd', 'f', 'g', 'h'],
                  'f': ['a', 'b', 'c', 'd', 'e', 'g', 'h'], 'g': ['a', 'b', 'c', 'd', 'e', 'f', 'h']}
    g.weights = {('a', 'b'): 1, ('b', 'a'): 1, ('a', 'c'): 1, ('c', 'a'): 1, ('a', 'd'): 1, ('d', 'a'): 1,
                 ('a', 'e'): 1, ('e', 'a'): 1, ('a', 'f'): 1, ('f', 'a'): 1, ('a', 'g'): 1, ('g', 'a'): 1,
                 ('a', 'h'): 1, ('h', 'a'): 1, ('b', 'c'): 1, ('c', 'b'): 1, ('b', 'd'): 1, ('d', 'b'): 1,
                 ('b', 'e'): 1, ('e', 'b'): 1, ('b', 'f'): 1, ('f', 'b'): 1, ('b', 'g'): 1, ('g', 'b'): 1,
                 ('b', 'h'): 1, ('h', 'b'): 1, ('c', 'd'): 1, ('d', 'c'): 1, ('c', 'e'): 1, ('e', 'c'): 1,
                 ('c', 'f'): 1, ('f', 'c'): 1, ('c', 'g'): 1, ('g', 'c'): 1, ('c', 'h'): 1, ('h', 'c'): 1,
                 ('d', 'e'): 1, ('e', 'd'): 1, ('d', 'f'): 1, ('f', 'd'): 1, ('d', 'g'): 1, ('g', 'd'): 1,
                 ('d', 'h'): 1, ('h', 'd'): 1, ('e', 'f'): 1, ('f', 'e'): 1, ('e', 'g'): 1, ('g', 'e'): 1,
                 ('e', 'h'): 1, ('h', 'e'): 1, ('f', 'g'): 1, ('g', 'f'): 1, ('f', 'h'): 1, ('h', 'f'): 1,
                 ('g', 'h'): 1, ('h', 'g'): 1}
    print(approx_tsp_tour(g))
