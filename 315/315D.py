H, W = map(int, input().split())
cookies = [list(input()) for _ in range(H)]
marked = [[False] * W for _ in range(H)]

for i in range(H):
    for j in range(W - 1):
        if cookies[i][j] == cookies[i][j + 1]:
            marked[i][j] = marked[i][j + 1] = True

for j in range(W):
    for i in range(H - 1):
        if cookies[i][j] == cookies[i + 1][j]:
            marked[i][j] = marked[i + 1][j] = True

new_cookies = []
for i in range(H):
    row = [cookies[i][j] for j in range(W) if not marked[i][j]]
    if row:
        new_cookies.append(row)

remaining_cookies = sum(len(row) for row in new_cookies)
print(remaining_cookies)

# WA 30