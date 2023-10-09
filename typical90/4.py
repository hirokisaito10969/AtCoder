H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

row_sums = [sum(row) for row in grid]
col_sums = [sum(col) for col in zip(*grid)]

for i in range(H):
    for j in range(W):
        print(row_sums[i] + col_sums[j] - grid[i][j], end=' ')
    print()

 #OK