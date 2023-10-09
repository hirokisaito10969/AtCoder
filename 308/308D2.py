def dfs(grid, i, j, k):
    if i < 0 or i >= H or j < 0 or j >= W or visited[i][j] or grid[i][j] != "snuke"[k]:
        return False

    if i == H - 1 and j == W - 1:
        return True

    visited[i][j] = True

    if dfs(grid, i + 1, j, (k + 1) % 5) or dfs(grid, i, j + 1, (k + 1) % 5):
        visited[i][j] = False
        return True

    visited[i][j] = False
    return False


# 入力の読み込み
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

visited = [[False] * W for _ in range(H)]

# 条件を満たす経路の存在判定
if H >= 2 and W >= 2 and dfs(grid, 0, 0, 0):
    print("Yes")
else:
    print("No")

# RE