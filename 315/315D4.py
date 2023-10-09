h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
x = [[0] * 26 for _ in range(h)]
y = [[0] * 26 for _ in range(w)]

for i in range(h):
    for j in range(w):
        x[i][ord(c[i][j]) - ord('a')] += 1
        y[j][ord(c[i][j]) - ord('a')] += 1

hc, wc = h, w
fx = [False] * h
fy = [False] * w

for _ in range(h + w):
    ux, uy = [], []
    for i in range(h):
        if fx[i]:
            continue
        for j in range(26):
            if x[i][j] == wc and wc >= 2:
                ux.append((i, j))
    for i in range(w):
        if fy[i]:
            continue
        for j in range(26):
            if y[i][j] == hc and hc >= 2:
                uy.append((i, j))
    for p in ux:
        fx[p[0]] = True
        for i in range(w):
            y[i][p[1]] -= 1
        hc -= 1
    for p in uy:
        fy[p[0]] = True
        for i in range(h):
            x[i][p[1]] -= 1
        wc -= 1

print(hc * wc)

# Answer from C++ TLE 33 pypyだとAC