n, m = map(int, input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]

print(s[0][-3:])

count = 0
for i in range(n):
    if s[i][-3:] in t:
        count += 1

print(count)
