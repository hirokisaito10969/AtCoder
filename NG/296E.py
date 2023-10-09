n = int(input())
a = list(map(int, input().split()))

win = set()
for i in range(1, n+1):
    x = i
    visited = set()
    while True:
        visited.add(x)
        x = a[x-1]
        if x in visited:
            if x == i:
                win.add(i)
            break

print(len(win))
