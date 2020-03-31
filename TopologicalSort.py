from collections import deque

from Graph import Digraph


def topological_sort(graph):
    sorted_list = []

    in_degrees = {v: 0 for v in graph.vertices()}
    for _, v2 in graph.edges():
        in_degrees[v2] += 1

    q = [k for k, v in in_degrees.items() if v == 0]
    while q:
        sorted_list.append(q.pop(0))
        for neighbor in graph.neighbors(sorted_list[-1]):
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                q.append(neighbor)

    return sorted_list


def topological_sort_dfs(graph):
    def _dfs_print_vertices(graph, vertex):
        nonlocal visited
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                _dfs_print_vertices(graph, neighbor)
            if neighbor not in sorted_list:
                sorted_list.appendleft(neighbor)

    sorted_list = deque()
    visited = set()
    for vertex in graph.vertices():
        if vertex not in visited:
            visited.add(vertex)
            _dfs_print_vertices(graph, vertex)
        if vertex not in sorted_list:
            sorted_list.appendleft(vertex)
    return list(sorted_list)


# def dfs_toposort1(G):
#     S, res = set(), []  # History and result
#
#     def recurse(u):  # Traversal subroutine
#         if u in S: return  # Ignore visited nodes
#         S.add(u)  # Otherwise: Add to history
#         for v in G.neighbors(u):
#             recurse(v)  # Recurse through neighbors
#         res.append(u)  # Finished with u: Append it
#
#     for u in G.vertices():
#         recurse(u)  # Cover entire graph
#     res.reverse()  # It's all backward so far
#     return res


# def topological_sort(graph):
#     sorted_vertices = []
#     visited = set()
#     for vertex in graph.vertices():
#         if vertex not in visited:
#             _topological_sort(graph, vertex, visited, sorted_vertices)
#     return sorted_vertices[::-1]
#
#
# def _topological_sort(graph, vertex, visited, sorted_vertices):
#     visited.add(vertex)
#     for adj in graph.adj_list[vertex]:
#         if adj not in visited:
#             _topological_sort(graph, adj, visited, sorted_vertices)
#     sorted_vertices.append(vertex)


if __name__ == '__main__':
    # cp3 4.4 dag in https://visualgo.net/en/dfsbfs
    dg = Digraph()
    dg.add_edge(0, 1)
    dg.add_edge(0, 2)
    dg.add_edge(1, 2)
    dg.add_edge(1, 3)
    dg.add_edge(2, 3)
    dg.add_edge(2, 5)
    dg.add_edge(3, 4)
    dg.add_edge(7, 6)
    print(topological_sort(dg))  # [0, 7, 1, 6, 2, 3, 5, 4]
    print(topological_sort_dfs(dg))  # [7, 6, 0, 1, 2, 5, 3, 4]
