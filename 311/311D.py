def dfs(grid, i, j):
    if i < 1 or i > len(grid) - 2 or j < 1 or j > len(grid[0]) - 2:
        return 0

    if grid[i][j] != '.':
        return 0

    grid[i][j] = '#'  # 探索済みの氷のルートとしてマークする

    count = 1

    count += dfs(grid, i - 1, j)
    count += dfs(grid, i + 1, j)
    count += dfs(grid, i, j - 1)
    count += dfs(grid, i, j + 1)

    return count

def count_ice_cells(grid):
    return dfs(grid, 2, 2)

# 入力を受け取る
N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = list(input().strip())
    grid.append(row)

result = count_ice_cells(grid)
print(result)
