n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sorted(a + b)
pos_a = [0] * n
pos_b = [0] * m

# Aの各要素がCの何番目にあるかを計算
for i in range(n):
    pos_a[i] = c.index(a[i]) + 1

# Bの各要素がCの何番目にあるかを計算
for i in range(m):
    pos_b[i] = c.index(b[i]) + 1

print(*pos_a)
print(*pos_b)
