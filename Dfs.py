from Graph import Digraph, Graph


def dfs(g):
    def _dfs(g, v):
        nonlocal time
        time += 1
        dtime[v] = time
        color[v] = GRAY
        for nb in g.neighbors(v):
            if color[nb] == WHITE:
                tree_edges.append((v, nb))
                pred[nb] = v
                _dfs(g, nb)
            elif color[nb] == GRAY:
                back_edges.append((v, nb))
            elif color[nb] == BLACK:
                if dtime[v] < dtime[nb]:
                    forward_edges.append((v, nb))
                else:
                    cross_edges.append((v, nb))
        color[v] = BLACK
        time += 1
        ftime[v] = time

    WHITE = 1  # unexplored
    GRAY = 2  # under exploration
    BLACK = 3  # finished exploration
    time = 0
    color = {}  # vertex color
    dtime = {}  # discovery time
    ftime = {}  # finishing time
    pred = {}  # predecessors of vertex
    tree_edges = []
    back_edges = []
    forward_edges = []
    cross_edges = []

    for v in g.vertices:  # initialize
        color[v] = WHITE
        pred[v] = None

    for v in g.vertices:  # main loop
        if color[v] == WHITE:
            _dfs(g, v)

    # dfs traversal done, print all relevant info
    for v in g.vertices:
        print(f'Vertex {v} - Dicovery/Finish time: {dtime[v]:2}/{ftime[v]:2}'
              f'   Predecessor: {pred[v]}')
    print(f'Tree edges   : {tree_edges}')
    print(f'Back edges   : {back_edges}')
    print(f'Forward edges: {forward_edges}')
    print(f'Cross edges  : {cross_edges}')
    # return dtime, ftime, pred, tree_edges, back_edges, forward_edges, cross_edges


def dfs_print_vertices(g):
    def dfs(g, vertex):
        for nb in g.neighbors(vertex):
            if nb not in visited:
                print(nb, end=' ')
                visited.add(nb)
                dfs(g, nb)

    visited = set()
    for v in g.vertices:
        if v not in visited:
            print(v, end=' ')
            visited.add(v)
            dfs(g, v)
    print('')


def dfs_vertices(g):
    def _dfs_vertices(g, vertex):
        for nb in g.neighbors(vertex):
            if nb not in visited:
                dfs_vert_arr.append(nb)
                visited.add(nb)
                _dfs_vertices(g, nb)

    dfs_vert_arr = []
    visited = set()
    for v in g.vertices:
        if v not in visited:
            dfs_vert_arr.append(v)
            visited.add(v)
            _dfs_vertices(g, v)
    return dfs_vert_arr


def dfs_print_vertices_iterative(g):
    visited = set()
    stack = []
    for v in g.vertices:
        if v not in visited:
            visited.add(v)
            stack = [v]
        while stack:
            vertex = stack.pop()
            print(vertex, end=' ')
            for nb in g.neighbors(vertex):
                if nb not in visited:
                    visited.add(nb)
                    stack.append(nb)
    print('')


# def dfs_print_vertices_iterative(g):
#     def _dfs_print_vertices_iterative(g, vertex):
#         stack = [vertex]
#         while stack:
#             vertex = stack.pop()
#             print(vertex, end=' ')
#             for nb in g.neighbors(vertex):
#                 if nb not in visited:
#                     visited.add(nb)
#                     stack.append(nb)
#
#     visited = set()
#     for v in g.vertices:
#         if v not in visited:
#             visited.add(v)
#             _dfs_print_vertices_iterative(g, v)
#     print('')


def dfs_path(g, source, target):
    def _dfs_path(g, source, target):
        for nb in g.neighbors(source):
            if nb == target:
                path.append(nb)
                return True
            elif nb not in visited:
                visited.add(nb)
                path.append(nb)
                if _dfs_path(g, nb, target):
                    return True
                path.pop()
        return False

    visited = set(source)
    path = [source]
    _dfs_path(g, source, target)
    return path if len(path) > 1 else []


def dfs_all_paths(g, source, target):
    def _dfs_all_paths(g, source, target):
        for nb in g.neighbors(source):
            if nb == target:
                all_paths.append(path + [nb])
            elif nb not in visited:
                visited.add(nb)
                path.append(nb)
                _dfs_all_paths(g, nb, target)
                path.pop()

    all_paths = []
    path = [source]
    visited = set(source)
    _dfs_all_paths(g, source, target)
    return all_paths


# def dfs(graph, source):
#     def _dfs(graph, vertex):
#         nonlocal visited, time
#         time += 1
#         dtime[vertex] = time
#         for neighbor in graph.neighbors(vertex):
#             if neighbor not in visited:
#                 pred[neighbor] = vertex
#                 visited.add(neighbor)
#                 _dfs(graph, neighbor)
#         time += 1
#         ftime[vertex] = time
#
#     visited = set()
#     time = 0
#     dtime = {}  # discovery time
#     ftime = {}  # finishing time
#     pred = defaultdict()  # predecessors of vertex
#     for vertex in graph.vertices:  # initialize
#         pred[vertex] = None
#
#     for vertex in graph.vertices:
#         if vertex not in visited:
#             visited.add(vertex)
#             _dfs(graph, vertex)
#
#     # print dfs paths
#     for vertex in graph.vertices:
#         if vertex == source:
#             continue
#         dfs_path = deque(vertex)
#         curr = vertex
#         while pred[curr] != source and pred[curr] is not None:
#             dfs_path.appendleft(pred[curr])
#             curr = pred[curr]
#         if pred[curr] is None:
#             dfs_path = []
#         else:
#             dfs_path.appendleft(pred[curr])
#         # print('path from ' + source + ' to ' + vertex + ' ' + str(bfs_path))
#         print(f'path from {source} to {vertex} : {str(list(dfs_path)):20}  '
#               f'discovery at {dtime[vertex]} finishing at {ftime[vertex]}')
#     print('')

if __name__ == '__main__':
    dg = Digraph()
    dg.add_edge('u', 'v')  # Cormen book example
    dg.add_edge('u', 'x')
    dg.add_edge('v', 'y')
    dg.add_edge('w', 'y')
    dg.add_edge('w', 'z')
    dg.add_edge('x', 'v')
    dg.add_edge('y', 'x')
    dg.add_edge('z', 'z')

    print('Digraph:', dg)
    print('Vertices:', dg.vertices)
    print('Edges:', dg.edges)
    print('')

    print('dfs print ', end='')
    dfs_print_vertices(dg)
    print('dfs print iterative ', end='')
    dfs_print_vertices_iterative(dg)

    print("dfs path from 'y' to 'v' ==> ", end='')
    print(dfs_path(dg, 'y', 'v'))
    print("dfs all paths from 'u' to 'v'  ==> ", end='')
    print(dfs_all_paths(dg, 'u', 'v'))
    print('')

    print('dfs')
    dfs(dg)
    print('')


