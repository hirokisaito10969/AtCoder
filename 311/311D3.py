def dfs(grid, visited, i, j):
    if i < 1 or i >= len(grid) - 1 or j < 1 or j >= len(grid[0]) - 1 or grid[i][j] == '#':
        # マスが範囲外または岩の場合、探索を終了
        return 0

    if visited[i][j]:
        # 既に訪れたマスの場合、探索を終了
        return 0

    visited[i][j] = True
    count = 1  # 現在のマスを含む氷の数

    # 上下左右の4方向を探索
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        count += dfs(grid, visited, i + dx, j + dy)

    return count

def count_ice(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    total_ice_count = 0

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if not visited[i][j] and grid[i][j] == '.':
                # 連結成分の氷の数を求める
                ice_count = dfs(grid, visited, i, j)
                total_ice_count += ice_count

    return total_ice_count

# 入力を受け取る
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# 出力
print(count_ice(grid))
