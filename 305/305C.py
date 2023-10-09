H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# 元々のクッキーが置かれていた部分長方形の範囲を求める
a, b, c, d = -1, -1, -1, -1
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            if a == -1:
                a = i
                b = i
                c = j
                d = j
            else:
                b = max(b, i)
                d = max(d, j)

# 元々のクッキーが置かれていた部分長方形の範囲を求める
aa, bb, cc, dd = -1, -1, -1, -1
for i in reversed(range(H)):
    for j in range(W):
        if grid[i][j] == '#':
            if aa == -1:
                aa = i
                bb = i
                cc = j
                dd = j
            else:
                bb = max(bb, i)
                dd = max(dd, j)
          
b = max(b,bb)
d = max(d,dd)
# すぬけ君が食べたクッキーの位置を特定する
for i in range(a, b + 1):
    for j in range(c, d + 1):
        if grid[i][j] == '.':
            print(i + 1, j + 1)
            exit()
