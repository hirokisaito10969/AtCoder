def is_tak_code(grid, i, j):
    if i + 8 >= len(grid) or j + 8 >= len(grid[0]):
        return False
    
    black_count = 0
    white_count = 0
    for x in range(i, i + 9):
        for y in range(j, j + 9):
            if grid[x][y] == '#':
                black_count += 1
            elif grid[x][y] == '.':
                white_count += 1
                        
    if black_count != 18 or white_count != 14:
        return False

    # Check the specific region for TaK Code condition
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            if grid[x][y] != '#':
                return False
    
    for x in range(i + 6, i + 9):
        for y in range(j + 6, j + 9):
            if grid[x][y] != '#':
                return False

    # Check neighbors in the 9x9 region
    neighbors = [(i, j+1), (i, j-1), (i+1, j), (i-1, j), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]
    for x, y in neighbors:
        if x < i or x >= i + 9 or y < j or y >= j + 9:  # Check if neighbor is inside the 9x9 region
            continue
        if grid[x][y] != '.':
            return False
    
    return True

def find_tak_codes(grid):
    tak_codes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_tak_code(grid, i, j):
                tak_codes.append((i + 1, j + 1))
    return tak_codes

def main():
    N, M = map(int, input().split())
    grid = [input() for _ in range(N)]
    
    tak_codes = find_tak_codes(grid)
    
    for i, j in tak_codes:
        print(i, j)

if __name__ == "__main__":
    main()
