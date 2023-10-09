dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(i, j):
    seen[i][j] = True
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if ni < 0 or ni >= H or nj < 0 or nj >= W:
            continue
        if grid[ni][nj] != next[grid[i][j]]:
            continue
        if seen[ni][nj]:
            continue
        dfs(ni, nj)

# Input reading
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

if grid[0][0] != 's':
    print("No")
    exit()

next = {'s': 'n', 'n': 'u', 'u': 'k', 'k': 'e', 'e': 's'}
seen = [[False] * W for _ in range(H)]

dfs(0, 0)
if seen[H - 1][W - 1]:
    print("Yes")
else:
    print("No")
