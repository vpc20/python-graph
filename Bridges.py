from Graph import Graph, is_connected


def bridges_naive(g):
    result = []
    for u, v in g.edges:
        g.remove_edge(u, v)
        if not is_connected(g):
            result.append((u, v))
        g.add_edge(u, v)
    return result


def bridges(g):
    def dfs(u, parent):
        nonlocal time
        seen.add(u)
        time += 1
        low[u] = dtime[u] = time

        for v in g.neighbors(u):
            if v == parent:
                continue
            if v not in seen:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if dtime[u] < low[v]:
                    result.append((u, v))
            else:
                low[u] = min(low[u], dtime[v])

    seen = set()
    time = 0
    dtime = {}  # discovery time
    low = {}  # min discovery time
    for u in g.vertices:
        dtime[u] = 0
        low[u] = 0

    result = []
    for u in g.vertices:
        if u not in seen:
            dfs(u, None)

    return result


# class Solution:
#     def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
#         graph = [[] for _ in range(n)]  ## vertex i ==> [its neighbors]
#
#     currentRank = 0  ## please note this rank is NOT the num (name) of the vertex itself, it is the order of your DFS level
#
#     lowestRank = [i for i in
#                   range(n)]  ## here lowestRank[i] represents the lowest order of vertex that can reach this vertex i
#
#     visited = [False for _ in range(n)]  ## common DFS/BFS method to mark whether this node is seen before
#
#     ## build graph:
#     for connection in connections:
#         ## this step is straightforward, build graph as you would normally do
#         graph[connection[0]].append(connection[1])
#         graph[connection[1]].append(connection[0])
#
#     res = []
#     prevVertex = -1  ## This -1 a dummy. Does not really matter in the beginning.
#     ## It will be used in the following DFS because we need to know where the current DFS level comes from.
#     ## You do not need to setup this parameter, I setup here ONLY because it is more clear to see what are passed on in the DFS method.
#
#     currentVertex = 0  ## we start the DFS from vertex num 0 (its rank is also 0 of course)
#     self._dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
#     return res
#
#
# def _dfs(self, res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):
#     visited[currentVertex] = True
#     lowestRank[currentVertex] = currentRank
#
#     for nextVertex in graph[currentVertex]:
#         if nextVertex == prevVertex:
#             continue  ## do not include the the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs.
#
#         if not visited[nextVertex]:
#             self._dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)
#         # We avoid visiting visited nodes here instead of doing it at the beginning of DFS -
#         # the reason is, even that nextVertex may be visited before, we still need to update my lowestRank using the visited vertex's information.
#
#         lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex])
#         # take the min of the current vertex's and next vertex's ranking
#         if lowestRank[
#             nextVertex] >= currentRank + 1:  ####### if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection ###
#             res.append([currentVertex, nextVertex])

if __name__ == '__main__':
    g = Graph()
    g.add_vertices_from([1, 2, 3, 4, 5, 6])
    g.add_edges_from([(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6), (3, 4)])
    # g.add_edges_from([(1, 2), (1, 3), (2, 3)])
    print(g)
    print(bridges(g))
    print(bridges_naive(g))
