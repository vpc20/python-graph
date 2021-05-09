# A topological sort of a dag G = (V, E) is a linear ordering of all its vertices such that if G contains an edge
# (u,v), then u appears before v in the ordering. (If the graph contains a cycle, then no linear ordering is
# possible.) We can view a topological sort of a graph as an ordering of its vertices along a horizontal line so
# that all directed edges go from left to right. Many applications use directed acyclic graphs to indicate
# precedences among events.

from collections import deque, defaultdict

from Graph import Digraph


def topological_sort(g):
    def dfs(g, u):
        seen.add(u)
        for v in g.neighbors(u):
            if v not in seen:
                dfs(g, v)
        sortedv.appendleft(u)

    seen = set()
    sortedv = deque()
    for u in g.vertices:
        if u not in seen:
            dfs(g, u)
    return list(sortedv)


def topological_sort2(g):
    result = []
    in_degrees = defaultdict(int)
    for u in g.vertices:
        in_degrees[u] += 0
        for v in g.neighbors(u):
            in_degrees[v] += 1
    # print(in_degrees)
    q = deque(k for k, v in in_degrees.items() if v == 0)
    # print(q)
    while q:
        u = q.popleft()
        result.append(u)
        for v in g.neighbors(u):
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                q.append(v)
    return result


# def topological_sort3(g):
#     in_degrees = defaultdict(int)
#
#     for u in g.vertices:
#         in_degrees[u] += 0
#         for v in g.neighbors(u):
#             in_degrees[v] += 1
#
#     list0 = [k for k, v in in_degrees.items() if v == 0]  # vertices with in-degree = 0
#     result = list0.copy()
#     for u in list0:
#         for v in g.neighbors(u):
#             in_degrees[v] -= 1
#             if in_degrees[v] == 0:
#                 result.append(v)
#
#     return result


if __name__ == '__main__':
    dress_order = [['shirt', 'tie'], ['tie', 'jacket'], ['belt', 'jacket'], ['shirt', 'belt'],
                   ['undershorts', 'pants'], ['undershorts', 'shoes'], ['pants', 'shoes'], ['pants', 'belt'],
                   ['socks', 'shoes']]
    g = Digraph()
    g.add_edges_from(dress_order)
    g.add_vertex('watch')
    print(g)
    print(topological_sort(g))
    print(topological_sort2(g))
