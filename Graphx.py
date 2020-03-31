from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(dict)

    def __str__(self):
        s = str(self.adj_list)
        return s[s.index('{'):-1]

    def vertices(self):
        return list(self.adj_list.keys())

    def number_of_vertices(self):
        return len(list(self.adj_list.keys()))

    def edges(self):
        return [(vertex, neighbor)
                for vertex in self.adj_list
                for neighbor in self.adj_list[vertex]]

    def number_of_edges(self):
        return len([(vertex, neighbor)
                    for vertex in self.adj_list
                    for neighbor in self.adj_list[vertex]])

    def neighbors(self, vertex):  # adjacent vertices
        return [neighbor for neighbor in self.adj_list[vertex]]

    def degree(self, vertex):  # number of adjacent vertices
        return len([neighbor for neighbor in self.adj_list[vertex]])

    def add_vertex(self, vertex):
        self.adj_list[vertex] = {}

    def remove_vertex(self, vertex):
        for edge in self.edges():
            if vertex in edge:
                self.remove_edge(edge[0], edge[1])
        self.adj_list.pop(vertex, None)

    # def add_edge(self, edge1, edge2, weight=1):
    #     neighbors_dict = self.adj_list[edge1]
    #     neighbors_dict[edge2] = weight
    #     self.adj_list[edge1] = neighbors_dict
    #
    #     neighbors_dict = self.adj_list[edge2]
    #     neighbors_dict[edge1] = weight
    #     self.adj_list[edge2] = neighbors_dict

    def add_edge(self, u, v, w=1):
        self.adj_list[u][v] = w
        self.adj_list[v][u] = w

    def remove_edge(self, u, v):
        self.adj_list[u].pop(v)
        # if not self.adj_list[u]:
        #     self.adj_list.pop(u)

        self.adj_list[v].pop(u)
        # if not self.adj_list[v]:
        #     self.adj_list.pop(v)

    def get_weight(self, u, v):
        return self.adj_list[u][v]

    def clear(self):
        self.adj_list.clear()


class Digraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, u, v, weight=1):
        self.adj_list[u][v] = weight
        if v not in self.adj_list:
            self.add_vertex(v)


def dfs_print_nodes(graph):
    def _dfs_print_nodes():
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                print(neighbor, end=' ')
                visited.add(neighbor)
                _dfs_print_nodes()

    visited = set()
    for node in graph.vertices():
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            _dfs_print_nodes()


# def dfs_print_nodes(graph):
#     visited = set()
#     for node in graph.nodes():
#         if node not in visited:
#             print(node, end=' ')
#             visited.add(node)
#             _dfs_print_nodes(graph, node, visited)
#
#
# def _dfs_print_nodes(graph, node, visited):
#     for neighbor in graph.neighbors(node):
#         if neighbor not in visited:
#             print(neighbor, end=' ')
#             visited.add(neighbor)
#             _dfs_print_nodes(graph, neighbor, visited)


def dfs_all_paths(graph, source, target):
    path = [source]
    all_paths = []
    _dfs_all_paths(graph, source, target, path, all_paths)
    return all_paths


def _dfs_all_paths(graph, source, target, path, all_paths):
    for neighbor in graph.neighbors(source):
        if neighbor == target:
            all_paths.append(path + [neighbor])
        elif neighbor not in path:
            path += [neighbor]
            _dfs_all_paths(graph, neighbor, target, path, all_paths)
            path.pop()


def bfs_print_nodes(graph):
    visited = set()
    queue = []
    for node in graph.vertices():
        if node not in visited:
            print(node, end=' ')
            queue.append(node)
            visited.add(node)
        while queue:
            node = queue.pop(0)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    print(neighbor, end=' ')
                    queue.append(neighbor)
                    visited.add(neighbor)


def bfs_all_paths(graph, source, target):
    all_paths = []
    queue = [[source]]
    while queue:
        for neighbor in graph.neighbors(queue[0][-1]):
            if neighbor == target:
                all_paths.append(queue[0] + [neighbor])
            elif neighbor not in queue[0]:
                queue.append(queue[0] + [neighbor])
        queue.pop(0)
    return all_paths


def topological_sort(graph):  # dfs traversal
    def _topological_sort(node):
        visited.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                _topological_sort(neighbor)
        sorted_vertices.append(node)

    sorted_vertices = []
    visited = set()
    for node in graph.vertices():
        if node not in visited:
            _topological_sort(node)
    return sorted_vertices[::-1]


def connected_components(graph):
    def _connected_components():
        for neighbor in graph.adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                # lst = connection_dict[cc_id]
                # lst.append(neighbor)
                # connection_dict[cc_id] = lst
                connection_dict[cc_id].append(neighbor)
                _connected_components()

    connection_dict = defaultdict(list)
    visited = set()
    cc_id = 0

    for node in graph.vertices():
        if node not in visited:
            visited.add(node)
            cc_id += 1
            # lst = connection_dict[cc_id]
            # lst.append(node)
            # connection_dict[cc_id] = lst
            connection_dict[cc_id].append(node)
            _connected_components()
    return [set(val) for val in connection_dict.values()]


def is_cyclic(graph):  # dfs traversal
    def _is_cyclic(node):
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                node_stack.append(neighbor)
                if _is_cyclic(neighbor):
                    return True
                node_stack.pop()
            else:
                if neighbor in node_stack:
                    return True

    visited = set()
    node_stack = []
    for node in graph.vertices():
        if node not in visited:
            visited.add(node)
            node_stack.append(node)
            if _is_cyclic(node):
                return True
            node_stack.pop()
    return False


# def _plain_bfs(g, source):
#     """A fast BFS node generator"""
#     seen = set()
#     nextlevel = {source}
#     while nextlevel:
#         thislevel = nextlevel
#         nextlevel = set()
#         for v in thislevel:
#             if v not in seen:
#                 yield v
#                 seen.add(v)
#                 nextlevel.update(g.adj_list[v])


if __name__ == '__main__':


    g = Graph()
    # g.add_node(1)
    # g.add_node(2)

    g.add_edge(1, 2, 9)
    g.add_edge(1, 3)
    g.add_edge(3, 2)
    g.add_edge(1, 4)
    g.add_edge(4, 2)
    g.add_edge(4, 3)
    g.add_edge(5, 6)

    # g.remove_edge(5, 6)

    print('Graph: ' + str(g))
    print('Nodes: ' + str(g.vertices()))
    # print('Number of Nodes: ' + str(g.number_of_nodes()))
    print('Edges: ' + str(g.edges()))
    # print('Number of Edges: ' + str(g.number_of_edges()))
    print(g.neighbors(1))
    print(g.degree(1))
    print(g.get_weight(1, 2))
    print('')

    print('dfs print nodes')
    dfs_print_nodes(g)
    print('')
    print('bfs print nodes')
    bfs_print_nodes(g)
    print('')

    print(dfs_all_paths(g, 1, 2))
    print('')
    print(bfs_all_paths(g, 1, 2))
    print('')

    # g.remove_edge(1, 3)
    # g.remove_node(3)
    # print('Graph: ' + str(g))
    # print('Nodes: ' + str(g.nodes()))
    # print('Edges: ' + str(g.edges()))
    # print(g.neighbors(2))

    # g.clear()
    # print('Graph: ' + str(g))
    # print('Nodes: ' + str(g.nodes()))
    # print('Edges: ' + str(g.edges()))
    print('-------------------------------------------------------------------')

    print(connected_components(g))

    # for item in _plain_bfs(g, 1):
    #     print(item)

    # dg = Digraph()
    # dg.add_edge(0, 1)
    # dg.add_edge(0, 2)
    # dg.add_edge(0, 4)
    # dg.add_edge(1, 3)
    # dg.add_edge(2, 3)
    # dg.add_edge(3, 5)
    # dg.add_edge(4, 5)
    #
    # print('Digraph:', dg)
    # print('Nodes:', dg.vertices())
    # print('Edges:', dg.edges())
    #
    # # print(topological_sort(dg))
    # print(is_cyclic(dg))
