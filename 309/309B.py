N = int(input())
grid = []
for _ in range(N):
    row = list(input())
    grid.append(row)

# 外側のマス目のコピーを作成
outer_grid = [row[:] for row in grid]

# 上辺のマス目を時計回りにずらして埋める
for j in range(N-1):
    outer_grid[0][j+1] = grid[0][j]

# 右辺のマス目を時計回りにずらして埋める
for i in range(N-1):
    outer_grid[i+1][N-1] = grid[i][N-1]

# 下辺のマス目を時計回りにずらして埋める
for j in range(N-1, 0, -1):
    outer_grid[N-1][j-1] = grid[N-1][j]

# 左辺のマス目を時計回りにずらして埋める
for i in range(N-1, 0, -1):
    outer_grid[i-1][0] = grid[i][0]

# 結果を出力
for row in outer_grid:
    print(''.join(row))
