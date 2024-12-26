from collections import defaultdict

matrix = [[9, 9, 4],
          [6, 6, 8],
          [2, 1, 1]]

nrows = len(matrix)
ncols = len(matrix[0])

# these are the nodes to be used
# m1 = [[] * ncols for _ in range(nrows)]
# for i in range(nrows):
#     for j in range(ncols):
#         m1[i].append(i * ncols + j)
# for row in m1:
#     print(row)

# g[m1[i][j]] += [m1[ix][jx]]


# g = defaultdict(list)
# vals = defaultdict(int)
# for i in range(nrows):
#     for j in range(ncols):
#         for ix, jx in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
#             if 0 <= ix < nrows and 0 <= jx < ncols:
#                 g[i * ncols + j] += [ix * ncols + jx]
#                 vals[i * ncols + j] = matrix[i][j]
# print(g)
# print(vals)

g = defaultdict(list)
for r in range(nrows):
    for c in range(ncols):
        for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
            if 0 <= nr < nrows and 0 <= nc < ncols:
                g[(r, c)].append((nr, nc))
for k, v in g.items():
    print(k, v)
