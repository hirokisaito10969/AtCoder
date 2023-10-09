N, X, Y = map(int, input().split())
r = [0] * 12
b = [0] * 12

r[1] = 0
b[1] = 1

for n in range(2, N + 1):
    b[n] = r[n - 1] + b[n - 1] * Y
    r[n] = r[n - 1] + b[n] * X

print(r[N])
