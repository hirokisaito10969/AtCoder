def count_ice_cells(N, M, grid):
    def is_ice(x, y):
        return 0 <= x < N and 0 <= y < M and grid[x][y] == '.'  # 修正

    def move(x, y, dx, dy):
        count = 0
        while is_ice(x + dx, y + dy):
            x += dx
            y += dy
            count += 1
        return x, y, count

    visited = set()
    stack = [(1, 1)]  # 初期位置を(1, 1)に修正
    visited.add((1, 1))  # 初期位置を(1, 1)に修正
    count = 0  # 初期値を0に修正

    while stack:
        x, y = stack.pop()
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for nx, ny in neighbors:
            if (nx, ny) not in visited and is_ice(nx, ny):
                stack.append((nx, ny))
                visited.add((nx, ny))
                x, y, cnt = move(nx, ny, nx - x, ny - y)
                count += cnt + 1  # プレイヤーが氷の上で停止できるので+1

    return count

# 入力を受け取る
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# 出力
result = count_ice_cells(N, M, grid)
print(result)
