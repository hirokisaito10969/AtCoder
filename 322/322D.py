def can_place(grid, polyomino, row, col):
    for i in range(len(polyomino)):
        for j in range(len(polyomino[0])):
            if polyomino[i][j] == '#' and (grid[row + i][col + j] == '#' or grid[row + i][col + j] == 'X'):
                return False
    return True

def place_polyomino(grid, polyomino, row, col):
    for i in range(len(polyomino)):
        for j in range(len(polyomino[0])):
            if polyomino[i][j] == '#':
                grid[row + i][col + j] = 'X'

def remove_polyomino(grid, polyomino, row, col):
    for i in range(len(polyomino)):
        for j in range(len(polyomino[0])):
            if polyomino[i][j] == '#':
                grid[row + i][col + j] = '.'

def is_valid(grid):
    for row in grid:
        if '.' in row:
            return False
    return True

def solve(grid, polyominos):
    if is_valid(grid):
        return True

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                for polyomino in polyominos:
                    if can_place(grid, polyomino, i, j):
                        place_polyomino(grid, polyomino, i, j)
                        if solve(grid, polyominos):
                            return True
                        remove_polyomino(grid, polyomino, i, j)

    return False

# 入力を受け取る
polyominos = []
for _ in range(3):
    polyomino = []
    for _ in range(4):
        row = input().strip()
        polyomino.append(list(row))
    polyominos.append(polyomino)

# 4x4の空のグリッドを作成
grid = [['.' for _ in range(4)] for _ in range(4)]

# 解を探索する
if solve(grid, polyominos):
    print("Yes")
else:
    print("No")
