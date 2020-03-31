from collections import defaultdict

from DisjointSet import DisjointSet
from Graph import transpose, Graph


def connected_components(g):
    """
    The connected components of a graph are the equivalence classes of vertices under 
    the “is reachable from” relation.
     
    :param g: input Graph 
    :return: list of sets containg the connected vertices
    """
    djset = DisjointSet()
    for v in g.vertices():
        djset.make_set(v)

    for v1, v2 in g.edges():
        if djset.find_set(v1) != djset.find_set(v2):
            djset.union(v1, v2)

    return djset.get_set()


# def connected_components_naive(graph):
#     djset = DisjointSet()
#
#     for vertex in graph.vertices():
#         djset.make_set(vertex)
#
#     for edge1, edge2 in graph.edges():
#         set1 = djset.find_set(edge1)
#         set2 = djset.find_set(edge2)
#         if set1 != set2:
#             djset.union(edge1, edge2)
#     return djset.disj_list


# def connected_components(graph):
#     djset = DisjointSet()
#     vertex_seq = defaultdict(str)
#     for i, vertex in enumerate(graph.vertices()):
#         vertex_seq[vertex] = i
#         djset.make_set(i)
#
#     for edge1, edge2 in graph.edges():
#         par1 = djset.find_set(vertex_seq[edge1])
#         par2 = djset.find_set(vertex_seq[edge2])
#         if par1 != par2:
#             djset.union(vertex_seq[edge1], vertex_seq[edge2])
#
#     parent_ids = djset.get()
#     # print(parent_ids)
#     conn_comps = defaultdict(set)
#     for i, vertex in enumerate(graph.vertices()):
#         conn_comps[parent_ids[i]].add(vertex)
#     return list(conn_comps.values())


def connected_components_dfs(graph):
    vlist = [v for v in graph.vertices()]
    _, ftime, _, _ = strongly_connected_dfs(graph, vlist)

    ftime_list = [(k, v) for k, v in ftime.items()]
    ftime_list.sort(key=lambda e: e[1], reverse=True)
    vlist = [v for v, _ in ftime_list]

    _, _, _, vert_dfs_tree = strongly_connected_dfs(graph, vlist)
    [set(item) for item in vert_dfs_tree.values()]
    return [set(item) for item in vert_dfs_tree.values()]


# def connected_components_dfs(graph):
#     def _connected_components(vertex):
#         for neighbor in graph.adj_list[vertex]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 conn_components[cc_id].add(neighbor)
#                 _connected_components(neighbor)
#
#     conn_components = defaultdict(set)
#     visited = set()
#     cc_id = 0
#
#     for vertex in graph.vertices():
#         if vertex not in visited:
#             visited.add(vertex)
#             cc_id += 1
#             conn_components[cc_id].add(vertex)
#             _connected_components(vertex)
#     return list(conn_components.values())

# def dfs_connection_dict(graph):
#     connected_dict = defaultdict(int)
#     visited = set()
#     cc_id = 0
#     for vertex in graph.vertices():
#         if vertex not in visited:
#             cc_id += 1
#             visited.add(vertex)
#             connected_dict[vertex] = cc_id
#             _dfs_connection_dict(graph, vertex, visited, cc_id, connected_dict)
#     return connected_dict
#
#
# def _dfs_connection_dict(graph, vertex, visited, cc_id, connected_dict):
#     for neighbor in graph.adj_list[vertex]:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             connected_dict[neighbor] = cc_id
#             _dfs_connection_dict(graph, neighbor, visited, cc_id, connected_dict)


def strongly_connected_components(g):
    """
    The strongly connected components of a directed graph are the equivalence classes of 
    vertices under the “are mutually reachable” relation.
     
    :param g: input graph
    :return: list of sets containing the strongly connected vertices
    """
    vert_list = [vertex for vertex in g.vertices()]
    _, ftime, _, _ = strongly_connected_dfs(g, vert_list)

    gt = transpose(g)

    ftime_list = [(k, v) for k, v in ftime.items()]
    ftime_list.sort(key=lambda e: e[1], reverse=True)
    vert_list = [v for v, _ in ftime_list]
    _, _, _, vert_dfs_tree = strongly_connected_dfs(gt, vert_list)
    return [set(val) for val in vert_dfs_tree.values()]


def strongly_connected_dfs(graph, vert_list):
    def _dfs(graph, vertex):
        nonlocal visited, time
        time += 1
        dtime[vertex] = time
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                vert_dfs_tree[cc_id].append(neighbor)
                pred[neighbor] = vertex
                visited.add(neighbor)
                _dfs(graph, neighbor)
        time += 1
        ftime[vertex] = time

    visited = set()
    time = 0
    dtime = defaultdict(int)  # discovery time
    ftime = defaultdict(int)  # finishing time
    pred = defaultdict()  # predecessors of vertex
    cc_id = 0
    vert_dfs_tree = defaultdict(list)  # vertices of each tree in the depth-first forest
    for vertex in graph.vertices():  # initialize
        pred[vertex] = None

    # for vertex in graph.vertices():
    for vertex in vert_list:
        if vertex not in visited:
            cc_id += 1
            vert_dfs_tree[cc_id].append(vertex)
            visited.add(vertex)
            _dfs(graph, vertex)
    return dtime, ftime, pred, vert_dfs_tree


if __name__ == '__main__':
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('e', 'f')
    g.add_edge('e', 'g')
    g.add_edge('h', 'i')
    g.add_vertex('j')
    print(connected_components(g))
    print(connected_components_dfs(g))

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_vertex(5)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    # [{6, 7, 8}, {5}, {0, 1, 2, 3, 4}]
    print(strongly_connected_components(g))


