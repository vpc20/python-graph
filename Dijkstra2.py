import sys
from heapq import heappop, heappush

# the adjacency list (dictionary) contain only edges, weight is a different dictionary
def dijkstra(g, src, tgt):
    dists = {}  # distances
    preds = {}  # predecessors
    for vertex in g.keys():
        dists[vertex] = sys.maxsize
        preds[vertex] = None
    dists[src] = 0
    minq = [(0, src)]  # minimum priority queue

    while minq:
        estimate_dist, vertex = heappop(minq)
        for neighbor in g[vertex]:  # breadth-first search
            estimate_dist = dists[vertex] + weight[(vertex, neighbor)]
            if estimate_dist < dists[neighbor]:  # relaxation
                dists[neighbor] = estimate_dist
                preds[neighbor] = vertex
                heappush(minq, (estimate_dist, neighbor))
    # get the path, since we produced the predecessors, the path is reversed
    vertex = tgt
    path = [vertex]
    while vertex != src:
        vertex = preds[vertex]
        path.append(vertex)
    path.reverse()

    return dists[tgt], path


# def dijkstra(g, src):
#     dist = {}  # distances
#     pred = {}  # predecessors
#     for u in g.vertices:
#         dist[u] = sys.maxsize
#         pred[u] = None
#     dist[src] = 0
#
#     minq = [(0, src)]
#     while minq:
#         d, u = heappop(minq)
#         if dist[u] < d:  # skip if the value in dist is smaller
#             continue
#         for v in g.neighbors(u):
#             d = dist[u] + g.weight(u, v)
#             if d < dist[v]:  # relaxation
#                 dist[v] = d
#                 pred[v] = u
#                 heappush(minq, (dist[v], v))  # could have duplicate vertices in minq
#     return pred, dist


# to get the path, refer to the predecessors dictionary


if __name__ == '__main__':
    # dg = Digraph()  # clrs example
    # dg.add_weighted_edges_from([('s', 't', 10), ('s', 'y', 5), ('t', 'x', 1), ('t', 'y', 2), ('x', 'z', 4),
    #                             ('y', 't', 3), ('y', 'x', 9), ('y', 'z', 2), ('z', 's', 7), ('z', 'x', 6)])
    # print(dg)
    # print(dijkstra(dg, 's'))

    # print('-----')
    # dg = Digraph()  # graph theory example youtube
    # dg.add_weighted_edges_from([(0, 1, 4), (0, 2, 1), (1, 3, 1), (2, 1, 2), (2, 3, 5), (3, 4, 3)])
    # print(dg)
    # print(dijkstra(dg, 0))
    #
    # print('-----')
    # # cp3 4.17 in https://visualgo.net/en/sssp
    # dg = Digraph()
    # dg.add_weighted_edges_from([(0, 1, 2), (0, 2, 6), (0, 3, 7), (1, 3, 3), (1, 4, 6),
    #                             (2, 4, 1), (3, 4, 5)])
    # print(dg)
    # print(dijkstra(dg, 0))

    g = {'s': ['t', 'y'], 't': ['x', 'y'], 'y': ['t', 'x', 'z'], 'x': ['z'], 'z': ['s', 'x']}
    # for k in g.keys():
    #     for v in g[k]:
    #         print(f'({k}, {v})')
    weight = {('s', 't'): 10,
              ('s', 'y'): 5,
              ('t', 'x'): 1,
              ('t', 'y'): 2,
              ('y', 't'): 3,
              ('y', 'x'): 9,
              ('y', 'z'): 2,
              ('x', 'z'): 4,
              ('z', 's'): 7,
              ('z', 'x'): 6}

    dist, path = dijkstra(g, 's', 'x')
    print(dist)
    print(path)
