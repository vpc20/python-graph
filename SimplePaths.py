# Give a linear-time algorithm that takes as input a directed acyclic graph G =(V, E) and two vertices
# two vertices s and t, and returns the simple paths from s to t in G. For example, the directed acyclic
# graph of Figure 22.8 contains exactly four simple paths from vertex p to vertex v:
# pov, poryv, posryv, and psryv.
# A simple path is a path with no repeated nodes
from collections import deque

from Graph import Digraph


def all_simple_paths_dfs(g, s, t):
    def dfs(g, u, path):
        if u == t:
            paths.append(path)
            return
        for v in g.neighbors(u):
            if v not in seen:
                seen.add(v)
                dfs(g, v, path + [v])
                seen.remove(v)  # backtrack

    seen = {s}
    paths = []
    dfs(g, s, [s])
    return paths


def all_simple_paths_bfs(g, s, t):
    paths = []
    queue = deque([(s, [s])])
    while queue:
        u, path = queue.popleft()
        if u == t:
            paths.append(path)
        else:
            for v in g.neighbors(u):
                queue.append((v, path +[v]))
    return paths


# def all_simple_paths_bfs(g, s, t):
#     seen = set()
#     paths = []
#     queue = deque([(s, s)])
#     while queue:
#         u, path = queue.popleft()
#         if u == t:
#             paths.append(path)
#         else:
#             for v in g.neighbors(u):
#                 if v not in seen:
#                     queue.append((v, path + v))
#                     seen.add(v)
#     return paths


if __name__ == '__main__':
    g = Digraph()  # clrs Figure 22.8
    g.add_edges_from([('m', 'q'), ('m', 'r'), ('m', 'x'), ('n', 'o'), ('n', 'q'), ('n', 'u'),
                      ('o', 'r'), ('o', 's'), ('o', 'v'), ('p', 'o'), ('p', 's'), ('p', 'z'), ('q', 't'),
                      ('r', 'u'), ('r', 'y'), ('s', 'r'), ('v', 'w'), ('v', 'x'), ('y', 'v')])
    print(all_simple_paths_dfs(g, 'p', 'v'))
    print(all_simple_paths_bfs(g, 'p', 'v'))
