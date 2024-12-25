import sys


def print_all_pairs_shortest_paths(verts, i, j):
    if i == j:
        print(i, end=' ')
    elif verts[i][j] is None:
        print(f'No path from {i} to {j} exists')
    else:
        print_all_pairs_shortest_paths(verts, i, verts[i][j])
        print(j, end=' ')


def floyd_warshall(wts):
    n = len(wts)
    d = [[wts[i][j] for j in range(n)] for i in range(n)]
    pred = [[i if i != j and wts[i][j] < sys.maxsize else None for j in range(n)]
            for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    pred[i][j] = pred[k][j]
    return pred, d


# def floyd_warshall(wts):
#     n = len(wts)
#     d = wts
#     pred = [[i if i != j and wts[i][j] < sys.maxsize else None
#              for j in range(n)]
#             for i in range(n)]
#
#     for k in range(1, n + 1):
#         for i in range(n):
#             for j in range(n):
#                 estd = d[i][k - 1] + d[k - 1][j]
#                 if estd < d[i][j]:
#                     d[i][j] = estd
#                     pred[i][j] = pred[k - 1][j]
#     return d, pred


# def floyd_warshall(wts):
#     n = len(wts)
#     d = [[[sys.maxsize] * n for _ in range(n)] for _ in range(n + 1)]
#     d[0] = wts
#     pred = [[[None] * n for _ in range(n)] for _ in range(n + 1)]
#     pred[0] = [[i if i != j and wts[i][j] < sys.maxsize else None
#                 for j in range(n)]
#                for i in range(n)]
#
#     for k in range(1, n + 1):
#         for i in range(n):
#             for j in range(n):
#                 estd = d[k - 1][i][k - 1] + d[k - 1][k - 1][j]
#                 if estd < d[k - 1][i][j]:
#                     d[k][i][j] = estd
#                     pred[k][i][j] = pred[k - 1][k - 1][j]
#                 else:
#                     d[k][i][j] = d[k - 1][i][j]
#                     pred[k][i][j] = pred[k - 1][i][j]
#     return d, pred


# def floyd_warshall(wts):
#     n = len(wts)
#     d = [[[sys.maxsize] * n for _ in range(n)] for _ in range(n + 1)]
#     d[0] = wts
#     pred = [[[None] * n for _ in range(n)] for _ in range(n + 1)]
#     pred[0] = [[i if i != j and wts[i][j] < sys.maxsize else None
#                 for j in range(n)]
#                for i in range(n)]
#     # print('pred')
#     # for row in pred[0]:
#     #     print(row)
#
#     for k in range(1, n + 1):
#         for i in range(n):
#             for j in range(n):
#                 d[k][i][j] = min(d[k - 1][i][j], d[k - 1][i][k - 1] + d[k - 1][k - 1][j])
#                 if i != j:
#                     if pred[k - 1][i][j] <= pred[k - 1][i][k - 1] + pred[k - 1][k - 1][j]:
#                         pred[k][i][j] = pred[k - 1][i][j]
#                     else:
#                         pred[k][i][j] = pred[k - 1][k - 1][j]
#     # return d[-1]
#     return pred


if __name__ == '__main__':
    n = 5
    weights = [[0, 3, 8, sys.maxsize, -4],
               [sys.maxsize, 0, sys.maxsize, 1, 7],
               [sys.maxsize, 4, 0, sys.maxsize, sys.maxsize],
               [2, sys.maxsize, -5, 0, sys.maxsize],
               [sys.maxsize, sys.maxsize, sys.maxsize, 6, 0]]

    # for row in weights:
    #     print(row)

    # ds, preds = floyd_warshall(weights)
    # for i, d in enumerate(ds):
    #     print(f'd[{i}]')
    #     for row in d:
    #         print(row)
    # for i, pred in enumerate(preds):
    #     print(f'pred[{i}]')
    #     for row in pred:
    #         print(row)

    d, pred = floyd_warshall(weights)
    for row in d:
        print(row)
    print('')

    for row in pred:
        print(row)
    print('')

    for row in pred:  # for comparison in clrs book result
        print([e + 1 if e is not None else None for e in row])
    print('')

    for i in range(n):
        for j in range(n):
            if i != j:
                print(f'path from {i} to {j}')
                print_all_pairs_shortest_paths(pred, i, j)
                print('')
    # print_all_pairs_shortest_paths(pred, 0, 1)
