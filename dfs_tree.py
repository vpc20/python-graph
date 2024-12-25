from Graph import Graph, Digraph


def dfs_tree(g, src):
    def dfs(g, u):
        for v in g.neighbors(u):
            if v not in seen:
                tree.add_edge(u, v)
                seen.add(v)
                dfs(g, v)

    tree = Graph()
    tree.add_vertex(src)
    seen = {src}
    dfs(g, src)
    return tree


if __name__ == '__main__':
    # dg = Digraph()  # clrs book example
    # dg.add_edges_from([('u', 'v'), ('u', 'x'), ('v', 'y'), ('w', 'y'),
    #                    ('w', 'z'), ('x', 'v'), ('y', 'x'), ('z', 'z')])
    # t = dfs_tree(dg, 'u')
    # print(t.vertices)
    # print(t.edges)

    dg = Digraph()
    # dg.add_edges_from([(0, 1), (1, 0), (2, 1)])
    dg.add_edges_from([(1, 0), (1, 4), (4, 0), (4, 2)])
    t = dfs_tree(dg, 0)
    print(t.vertices)
    print(t.edges)
