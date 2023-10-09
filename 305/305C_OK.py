H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# クッキーが置かれている部分長方形の左上と右下の座標を探す
left = float('inf')
top = float('inf')
right = -float('inf')
bottom = -float('inf')

for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            left = min(left, j)
            top = min(top, i)
            right = max(right, j)
            bottom = max(bottom, i)

# すぬけ君が食べたクッキーの座標を求める
for i in range(top, bottom + 1):
    for j in range(left, right + 1):
        if grid[i][j] == '.':
            print(i + 1, j + 1)
            exit()
