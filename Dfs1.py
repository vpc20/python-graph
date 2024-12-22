def dfs(g):
    def _dfs(g, vertex):
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in g[vertex]:
            if neighbor not in visited:
                _dfs(g, neighbor)

    visited = set()
    for vertex in g.keys():
        if vertex not in visited:
            _dfs(g, vertex)
    print()


# g = {'s': ['t', 'y'], 't': ['x', 'y'], 'y': ['t', 'x', 'z'], 'x': ['z'], 'z': ['s', 'x']}
# weight = {('s', 't'): 10,
#           ('s', 'y'): 5,
#           ('t', 'x'): 1,
#           ('t', 'y'): 2,
#           ('y', 't'): 3,
#           ('y', 'x'): 9,
#           ('y', 'z'): 2,
#           ('x', 'z'): 4,
#           ('z', 's'): 7,
#           ('z', 'x'): 6}
g = {'u': ['v', 'x'], 'v': ['y'], 'x': ['v'], 'y': ['x'], 'w': ['y', 'z'], 'z': ['z']}
dfs(g)
