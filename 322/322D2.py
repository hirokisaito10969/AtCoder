def is_valid_placement(grid, piece, row, col):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == '#' and grid[row + i][col + j] == '#':
                return False
    return True

def place_piece(grid, piece, row, col):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == '#':
                grid[row + i][col + j] = '#'

def remove_piece(grid, piece, row, col):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == '#':
                grid[row + i][col + j] = '.'

def can_fill_grid(grid, pieces, piece_index):
    if piece_index == len(pieces):
        return True
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if is_valid_placement(grid, pieces[piece_index], row, col):
                place_piece(grid, pieces[piece_index], row, col)
                if can_fill_grid(grid, pieces, piece_index + 1):
                    return True
                remove_piece(grid, pieces[piece_index], row, col)
    
    return False

def solve_puzzle(pieces):
    grid_size = 4
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    
    if can_fill_grid(grid, pieces, 0):
        return "Yes"
    else:
        return "No"

# 入力を受け取る
pieces = []
for _ in range(3):
    piece = []
    for _ in range(4):
        row = input().strip()
        piece.append(row)
    pieces.append(piece)

result = solve_puzzle(pieces)
print(result)
