from collections import defaultdict


class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x):
        # self.parent.append(x)
        # self.rank.append(0)
        self.parent[x] = x
        self.rank[x] = 0

    def find_set(self, x):  # use path compression
        if x != self.parent[x]:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    # def find_set(self, x):  # use path compression
    #     xlist = []
    #     while x != self.parent[x]:
    #         xlist.append(x)
    #         x = self.parent[x]
    #     for i in xlist:
    #         self.parent[i] = self.parent[x]
    #     # while xlist:
    #     #     self.parent[xlist.pop()] = self.parent[x]
    #     return self.parent[x]

    def link(self, x, y):  # union by rank
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    def get_set(self):
        conn_comps = defaultdict(set)
        for k, val in self.parent.items():
            conn_comps[val].add(k)
        return list(conn_comps.values())


if __name__ == '__main__':
    djset = DisjointSet()
    djset.make_set('a')
    djset.make_set('b')
    djset.make_set('c')
    print(djset.parent)

    djset.union('a', 'b')
    print(djset.parent)

    print(djset.find_set('a'))
    print(djset.find_set('b'))
    print(djset.find_set('c'))

    print(djset.get_set())

