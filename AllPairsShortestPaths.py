import sys


def print_all_pairs_shortest_paths(verts, i, j):
    if i == j:
        print(i, end=' ')
    elif verts[i][j] is None:
        print(f'No path from {i} to {j} exists')
    else:
        print_all_pairs_shortest_paths(verts, i, verts[i][j])
        print(j, end=' ')


# def extend_shortest_paths(l, wts):  # correct
#     n = len(l)
#     lp = [[sys.maxsize] * n for _ in range(n)]  # shortest path weights
#
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 lp[i][j] = min(lp[i][j], l[i][k] + wts[k][j])
#     return lp


def extend_shortest_paths(l, v, wts):  # correct
    n = len(l)
    lp = [[sys.maxsize] * n for _ in range(n)]  # shortest path weights
    vp = [[[]] * n for _ in range(n)]  # shortest path vertices

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if l[i][k] != sys.maxsize and wts[k][j] != sys.maxsize:
                    lp[i][j] = min(lp[i][j], l[i][k] + wts[k][j])
                # if l[i][j] <= l[i][k] + l[k][j]:
                #     vp[i][j] = v[i][j]
                # else:
                #     vp[i][j] = v[k][j]
                if l[i][k] + wts[k][j] < lp[i][j]:
                    v[i][j].append(k)
                # else:
                #     vp[k][j] = k
    return lp, v


# def extend_shortest_paths(l, weights):
#     n = len(l)
#     lp = [[sys.maxsize] * n for _ in range(n)]  # shortest path weights
#     # vp = [[None] * n for _ in range(n)]  # shortest path vertices
#
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 # lp[i][j] = min(lp[i][j], l[i][k] + weights[k][j])
#                 if l[i][k] + weights[k][j] < lp[i][j]:
#                     lp[i][j] = l[i][k] + weights[k][j]
#                     # vp[i][j] = j
#     # print(f'vs: {vp}')
#     return lp  # , vp


# def slow_all_pairs_shortest_paths(wts):  # correct
#     n = len(wts)
#     l = [wts]
#     for m in range(1, n - 1):
#         lp = extend_shortest_paths(l[m - 1], wts)
#         l.append(lp)
#     return l


def slow_all_pairs_shortest_paths(wts):
    n = len(wts)

    # l = [wts]
    lx = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    for i in range(n):
        lx[i][i] = 0
    l = [lx]

    # vs = [[None] * n for _ in range(n)]
    # for i in range(n):  # vs[0]
    #     for j in range(n):
    #         if i != j and wts[i][j] < sys.maxsize:
    #             vs[i][j] = i
    # vs = [[[]] * n for _ in range(n)]
    # v = [vs]
    v = [[[] for _ in range(n)] for _ in range(n)]

    for m in range(1, n):
        lp, v = extend_shortest_paths(l[m - 1], v, wts)
        # if m == 1:
        #     l.append(wts)
        # else:
        #     l.append(lp)
        l.append(lp)
        # v.append(vp)
    return l, v


# def slow_all_pairs_shortest_paths(weights):
#     n = len(weights)
#     l = [[[sys.maxsize for _ in range(n)] for _ in range(n)] for _ in range(2)]
#     for i in range(n):
#         l[0][i][i] = 0
#     l[1] = weights  # l[1] = weights
#     vs = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]  # shortest path vertices
#
#     for m in range(2, n):
#         lp = extend_shortest_paths(l[m - 1], weights)
#         l.append(lp)
#         # vs.append(vp)
#         # print(f'l[{m}] : {l[m]}')
#         # print(f'vs[{m}]: {vs[m]}')
#
#     # create vertices matrix
#     for i in range(n):  # vs[0]
#         for j in range(n):
#             if i == j or weights[i][j] == sys.maxsize:
#                 vs[0][i][j] = None
#             if i != j and weights[i][j] < sys.maxsize:
#                 vs[0][i][j] = i
#
#     for i in range(n):  # vs
#         for j in range(n):
#             for k in range(1, n):
#                 if l[k - 1][i][j] <= l[k - 1][i][k] + l[k - 1][k][j]:
#                     vs[k][i][j] = vs[k - 1][i][j]
#                 else:
#                     vs[k][i][j] = vs[k - 1][k][j]
#                 # print(f'vs[{k}][{i}][{j}] = {vs[k][i][j]}')
#
#     # print('vs'* 16)
#     # for i, item in enumerate(vs):
#     #     print(f'vs[{i}] --------------------------------')
#     #     for subitem in item:
#     #         print(subitem)
#
#     return l, vs

if __name__ == '__main__':
    vs1 = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
    vs2 = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
    n = len(vs1)
    weights = [[sys.maxsize] * n for _ in range(n)]
    for i in range(n):
        weights[i][i] = 0
    weights[vs1[1]][vs1[2]] = 3
    weights[vs1[1]][vs1[3]] = 8
    weights[vs1[1]][vs1[5]] = -4
    weights[vs1[2]][vs1[4]] = 1
    weights[vs1[2]][vs1[5]] = 7
    weights[vs1[3]][vs1[2]] = 4
    weights[vs1[4]][vs1[1]] = 2
    weights[vs1[4]][vs1[3]] = -5
    weights[vs1[5]][vs1[4]] = 6

    for i in range(n):
        for j in range(n):
            if weights[i][j] != 0:
                print(f'edge ({vs2[i]}, {vs2[j]})  w = {weights[i][j]}')
    print('weights')
    for item in weights:
        print(item)
    # print('-' * 64)

    # print('extend_shortest_paths')
    # lx = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    # for i in range(n):
    #     lx[i][i] = 0
    # vs = [[None] * n for _ in range(n)]
    # for i in range(n):  # vs[0]
    #     for j in range(n):
    #         if i != j and weights[i][j] < sys.maxsize:
    #             vs[i][j] = i
    # print(extend_shortest_paths(lx, vs, weights))

    # l1 = [[0, 3, 8, 9223372036854775807, -4], [9223372036854775807, 0, 9223372036854775802, 1, 7], [9223372036854775807, 4, 0, 9223372036854775807, 9223372036854775803], [2, 9223372036854775807, -5, 0, 9223372036854775803], [9223372036854775807, 9223372036854775807, 9223372036854775802, 6, 0]]
    # print(extend_shortest_paths(l1, weights))
    # l2 = [[0, 3, 8, 2, -4], [3, 0, -4, 1, 7], [9223372036854775807, 4, 0, 5, 11], [2, -1, -5, 0, -2], [8, 9223372036854775806, 1, 6, 0]]
    # print(extend_shortest_paths(l2, weights))
    # l3 = [[0, 3, -3, 2, -4], [3, 0, -4, 1, -1], [7, 4, 0, 5, 11], [2, -1, -5, 0, -2], [8, 5, 1, 6, 0]]
    # print(extend_shortest_paths(l3, weights))

    l, v = slow_all_pairs_shortest_paths(weights)
    # l, vs = slow_all_pairs_shortest_paths(weights)

    print('slow_all_pairs_shortest_paths')
    print(l)
    for i, item1 in enumerate(l):
        print(f'l[{i}]')
        for item2 in item1:
            print(item2)
        print('-' * 64)
    # for i, item1 in enumerate(v):
    #     print(f'v[{i}]')
    #     for item2 in item1:
    #         print(item2)
    #     print('-' * 64)
    for item in v:
        print(item)

    # verts = [[None, 2, 3, 4, 0],
    #          [3, None, 3, 1, 0],
    #          [3, 2, None, 1, 0],
    #          [3, 2, 3, None, 0],
    #          [3, 2, 3, 4, None]]
    # print_all_pairs_shortest_paths(verts, 0, 1)
    # print('')
    # print_all_pairs_shortest_paths(verts, 0, 3)
    # print('')
    # print_all_pairs_shortest_paths(verts, 3, 0)
