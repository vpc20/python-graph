# The transpose of a directed graph G=(V, E) is the graph Gᵀ = (V, Eᵀ) , where
# Eᵀ = {(v,u) ∈ V x V : (u,v) ∈ E}. Thus, GT is G with all its edges reversed.
from Graph import Digraph


def transpose(g):
    gt = Digraph()
    for u in g.vertices:
        gt.add_vertex(u)
    for u, v in g.edges:
        gt.add_edge(v, u, g.weight(u, v))
    return gt


if __name__ == '__main__':
    g = Digraph()
    g.add_edges_from([('a', 'b'), ('b', 'c'), ('b', 'e'), ('b', 'f'), ('c', 'd'), ('c', 'g'), ('d', 'c'),
                      ('d', 'h'), ('e', 'a'), ('e', 'f'), ('f', 'g'), ('g', 'f'), ('g', 'h'), ('h', 'h')])
    gt = transpose(g)
    print(gt.edges)