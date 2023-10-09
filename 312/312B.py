def check_tak_code_region(grid, i, j):
    # 9マス×9マスの領域を確認
    for x in range(i, i + 9):
        for y in range(j, j + 9):
            # 左上及び右下の縦3マス横3マスの18マスが全て黒であるかを確認
            if x < i + 3 and y < j + 3 and grid[x][y] == '.':
                return False
            # 左上及び右下の縦3マス横3マスに八方位で隣接する14マスが全て白であるかを確認
            elif x >= i + 3 and y >= j + 3 and grid[x][y] == '#':
                return False

    return True

def find_tak_codes(N, M, grid):
    tak_codes = []
    for i in range(N - 8):
        for j in range(M - 8):
            if check_tak_code_region(grid, i, j):
                tak_codes.append((i + 1, j + 1))  # 1-indexed coordinates

    return tak_codes

# 入力を受け取る
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# TaK Code の条件を満たす領域を探索
result = find_tak_codes(N, M, grid)

# 結果を出力
for i, j in result:
    print(i, j)
