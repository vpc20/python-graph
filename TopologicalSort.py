# A topological sort of a dag G = (V, E) is a linear ordering of all its vertices such that if G contains an edge
# (u,v), then u appears before v in the ordering. (If the graph contains a cycle, then no linear ordering is
# possible.) We can view a topological sort of a graph as an ordering of its vertices along a horizontal line so
# that all directed edges go from left to right. Many applications use directed acyclic graphs to indicate
# precedences among events.

from collections import deque

from Graph import Digraph


def topological_sort(g):
    def dfs(g, u):
        for v in g.neighbors(u):
            if v not in seen:
                dfs(g, v)
                seen.add(v)
        sortedv.appendleft(u)

    seen = set()
    sortedv = deque()
    for u in g.vertices:
        if u not in seen:
            dfs(g, u)
            seen.add(u)
    return sortedv


if __name__ == '__main__':
    dress_order = [['shirt', 'tie'], ['tie', 'jacket'], ['belt', 'jacket'], ['shirt', 'belt'],
                   ['undershorts', 'pants'], ['pants', 'shoes'], ['socks', 'shoes']]
    g = Digraph()
    g.add_edges_from(dress_order)
    g.add_vertex('jacket')
    g.add_vertex('watch')
    g.add_vertex('shoes')
    print(g)
    print(topological_sort(g))
