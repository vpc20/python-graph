import sys
from collections import defaultdict, deque
from Graph import Graph


def bfs(g, source):
    dist = defaultdict(int)  # distances from source to vertex
    pred = defaultdict()  # predecessors of vertex
    for v in g.vertices:  # initialize
        dist[v] = sys.maxsize
        pred[v] = None
    dist[source] = 0

    tree_edges = []
    visited = set(source)
    queue = deque(source)
    while queue:
        v = queue.popleft()
        for nb in g.neighbors(v):
            if nb not in visited:
                tree_edges.append((v, nb))
                dist[nb] = dist[v] + g.weight(v, nb)
                pred[nb] = v
                queue.append(nb)
                visited.add(nb)

    # print all paths
    for v in g.vertices:
        if v == source:
            continue
        if dist[v] == sys.maxsize:  # no path exists from source to v
            print(f'path from {source} to {v} : []  distance is 0')
            continue
        bfs_path = deque(v)
        curr = v
        while pred[curr] != source:
            bfs_path.appendleft(pred[curr])
            curr = pred[curr]
        bfs_path.appendleft(source)
        print(f'path from {source} to {v} : {str(list(bfs_path)):20}  distance is {dist[v]}')
    print(f'Tree edges : {tree_edges}')
    print('')


def bfs_print_vertices(g):
    visited = set()
    queue = []
    for v in g.vertices:
        if v not in visited:
            print(v, end=' ')
            queue = [v]
            visited.add(v)
        while queue:
            vertex = queue.pop(0)
            for nb in g.neighbors(vertex):
                if nb not in visited:
                    print(nb, end=' ')
                    queue.append(nb)
                    visited.add(nb)
    print('')


def bfs_shortest_path(g, source, target):
    queue = [[source]]
    while queue:
        for nb in g.neighbors(queue[0][-1]):
            if nb == target:
                return queue[0] + [nb]
            elif nb not in queue[0]:
                queue.append(queue[0] + [nb])
        queue.pop(0)


def bfs_all_shortest_path(g, source, target):
    all_shortest = []
    queue = [[source]]
    while queue:
        for nb in g.neighbors(queue[0][-1]):
            if all_shortest and len(queue[0] + [nb]) > len(all_shortest[0]):
                break
            if nb == target:
                all_shortest.append(queue[0] + [nb])
            elif nb not in queue[0]:
                queue.append(queue[0] + [nb])
        queue.pop(0)
    return all_shortest


def bfs_all_paths(g, source, target):
    all_paths = []
    queue = [[source]]
    while queue:
        for nb in g.neighbors(queue[0][-1]):
            if nb == target:
                all_paths.append(queue[0] + [nb])
            elif nb not in queue[0]:
                queue.append(queue[0] + [nb])
        queue.pop(0)
    return all_paths


# def bfs_shortest_path1(graph, source, target):
#     all_paths = [[source]]
#     queue = [source]
#     while queue:
#         for neighbor in graph.neighbors(queue.pop(0)):
#             if neighbor == target:
#                 return all_paths[0] + [neighbor]
#             elif neighbor not in queue:
#                 queue.append(neighbor)
#                 all_paths.append(all_paths[0] + [neighbor])
#         all_paths.pop(0)

if __name__ == '__main__':
    g = Graph()
    g.add_edge('r', 's')
    g.add_edge('r', 'v')
    g.add_edge('s', 'w')
    g.add_edge('t', 'u')
    g.add_edge('t', 'w')
    g.add_edge('t', 'x')
    g.add_edge('u', 'x')
    g.add_edge('u', 'y')
    g.add_edge('w', 'x')
    g.add_edge('x', 'y')

    print('Graph   :', g)
    print('Vertices:', g.vertices)
    print('Edges   :', g.edges)
    print('Weights :', g.weights)

    print('bfs print vertices ', end='')
    bfs_print_vertices(g)

    print("bfs shortest path from 's' to 'u' ==> ", end='')
    print(bfs_shortest_path(g, 's', 'u'))
    print("bfs all shortest path from 's' to 'u' ==> ", end='')
    print(bfs_all_shortest_path(g, 's', 'u'))
    print("bfs all paths from 's' to 'u' ==> ", end='')
    print(bfs_all_paths(g, 's', 'u'))

    print('---------- bfs ----------')
    bfs(g, 's')
    print('')

    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('d', 'e')
    print('---------- bfs ----------')
    bfs(g, 'a')
    print('')
