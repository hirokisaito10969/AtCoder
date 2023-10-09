H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# 上下左右と斜めの4つの方向を定義
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# マス目を走査して条件を満たす場所を見つける
for i in range(H):
    for j in range(W):
        if grid[i][j] == 's':
            # 上下左右と斜めの方向に連続しているか確認
            for dx, dy in directions:
                ni, nj = i, j
                cnt = 0
                while 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == 'snuke'[cnt]:
                    cnt += 1
                    ni += dx
                    nj += dy
                    if cnt == 5:
                        # 条件を満たす場所を出力
                        print(i + 1, j + 1)
                        print(i + 1 + 1 * dx, j + 1 + 1 * dy)
                        print(i + 1 + 2 * dx, j + 1 + 2 * dy)
                        print(i + 1 + 3 * dx, j + 1 + 3 * dy)
                        print(i + 1 + 4 * dx, j + 1 + 4 * dy)
                        exit()
