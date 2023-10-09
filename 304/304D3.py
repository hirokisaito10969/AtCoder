w, h = map(int, input().split())
n = int(input())
p = [0] * (n + 1)
q = [0] * (n + 1)
for i in range(1, n + 1):
    p[i], q[i] = map(int, input().split())
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))
a.append(w)
b.append(h)

mp = {}
for i in range(1, n + 1):
    X = next(x for x in a[1:] if x >= p[i])
    Y = next(y for y in b[1:] if y >= q[i])
    mp[(X, Y)] = mp.get((X, Y), 0) + 1

m = n
M = max(mp.values())
if len(mp) == (A + 1) * (B + 1):
    m = min(mp.values())
else:
    m = 0
print(m, M)
