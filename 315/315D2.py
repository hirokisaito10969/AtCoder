H, W = map(int, input().split())
cookies = [list(input()) for _ in range(H)]
marked = [[False] * W for _ in range(H)]

def mark_cookies():
    for i in range(H):
        for j in range(W - 1):
            if cookies[i][j] == cookies[i][j + 1]:
                marked[i][j] = marked[i][j + 1] = True

    for j in range(W):
        for i in range(H - 1):
            if cookies[i][j] == cookies[i + 1][j]:
                marked[i][j] = marked[i + 1][j] = True

def remove_marked_cookies():
    for i in range(H):
        for j in range(W):
            if marked[i][j]:
                cookies[i][j] = '.'
    return sum(row.count('.') for row in cookies)

remaining_cookies = H * W

while True:
    mark_cookies()
    removed_count = remove_marked_cookies()
    if removed_count == 0:
        break
    remaining_cookies -= removed_count

print(remaining_cookies)

# TLE 39 pypyでもTLEになりそう CPython 2212ms pypy 2222ms