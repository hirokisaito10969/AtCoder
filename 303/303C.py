def can_complete_moves(N, M, H, K, S, items):
    x, y = 0, 0
    item_set = set(items)
    for i in range(N):
        if S[i] == 'R':
            x += 1
        elif S[i] == 'L':
            x -= 1
        elif S[i] == 'U':
            y += 1
        elif S[i] == 'D':
            y -= 1
            
        H -= 1

        # Check if health is negative
        if H < 0:
            return False
        
        # Check if there is an item at the current position
        if H < K:
            if (x, y) in item_set:
                H = K  # Consume the item and restore health
                item_set.remove((x, y))
                # H += 1

    return True


# Read input
N, M, H, K = map(int, input().split())
S = input()
items = []
for _ in range(M):
    x, y = map(int, input().split())
    items.append((x, y))

# Check if moves can be completed
result = can_complete_moves(N, M, H, K, S, items)

# Print the result
if result:
    print("Yes")
else:
    print("No")
