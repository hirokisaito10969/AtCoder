from collections import deque

def is_valid(x, y, H, W):
    return 0 <= x < H and 0 <= y < W

def solve_field(H, W, field):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Find the positions of S and G
    start_x, start_y = None, None
    goal_x, goal_y = None, None
    for i in range(H):
        for j in range(W):
            if field[i][j] == 'S':
                start_x, start_y = i, j
            elif field[i][j] == 'G':
                goal_x, goal_y = i, j
    
    # BFS to find the shortest path without entering sight lines
    visited = set()
    queue = deque([(start_x, start_y, 0)])
    while queue:
        x, y, moves = queue.popleft()
        
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        if x == goal_x and y == goal_y:
            return moves
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, H, W) and field[new_x][new_y] != '#' and (new_x, new_y) not in visited:
                queue.append((new_x, new_y, moves + 1))
    
    return -1

# Read input
H, W = map(int, input().split())
field = []
for _ in range(H):
    row = input()
    field.append(row)

# Calculate and print the answer
answer = solve_field(H, W, field)
print(answer)
