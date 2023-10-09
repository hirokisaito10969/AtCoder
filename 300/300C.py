# import numpy as np

# H, W = map(int, input().split())
# A = [list(input().strip()) for _ in range(H)]

# list1 = [0] * H

# for i in range(-H, H):
#     AA = np.diag(A, k = i)
#     if "#" in AA:
#         AAA = map(len, AA)
#         AAAA = map(lambda x: (x-1) // 2, AAA)
#         AAAAB = list(map(abs, AAAA))
#         for j in len(AAAAB):
#             if AAAAB[j] != 0:
#                 list1[j] += 1

# for i in range(len(list1)):
#     print(list1[i])

# H, W = map(int, input().split())
# C = [list(input()) for _ in range(H)]

# def dfs(y, x):
#     cnt = 1
#     C[y][x] = '.'
#     for dy in range(-1, 2):
#         for dx in range(-1, 2):
#             y2, x2 = y + dy, x + dx
#             if 0 <= y2 < H and 0 <= x2 < W and C[y2][x2] == '#':
#                 cnt += dfs(y2, x2)
#     return cnt

# ans = [0 for _ in range(min(H, W))]
# for y in range(H):
#     for x in range(W):
#         if C[y][x] == '#':
#             ans[dfs(y, x) // 4 - 1] += 1
# print(' '.join(map(str, ans)))

H, W = map(int, input().split())
g = []
for _ in range(H):
    row = input()
    g.append(row)

def ok(i, j):
    return 0 <= i < H and 0 <= j < W

def test(i, j, d):
    for x in [+d, -d]:
        for y in [+d, -d]:
            s = i + x
            t = j + y
            if not ok(s, t) or g[s][t] != '#':
                return False
    return True

N = min(H, W)
ans = [0] * (N + 1)
for i in range(H):
    for j in range(W):
        if g[i][j] != '#':
            continue
        if test(i, j, 1):
            d = 1
            while test(i, j, d + 1):
                d += 1
            ans[d] += 1

for i in range(1, N + 1):
    print(ans[i], end=' ')
print()
