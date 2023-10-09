from fractions import Fraction
from decimal import Decimal

N = int(input())
data = []

for i in range(1, N + 1):
    A, B = map(int, input().split())
    success_rate = Decimal(A) / Decimal(A + B)
    data.append((success_rate, i))

data.sort(key=lambda x: (-x[0], x[1]))  # 成功率の降順にソート

# 成功率が等しい場合にのみ再比較
i = 0
while i < N - 1:
    j = i + 1
    while j < N and data[j][0] == data[i][0]:
        fraction_i = Fraction(data[i][0]).limit_denominator()
        fraction_j = Fraction(data[j][0]).limit_denominator()
        if fraction_j > fraction_i:
            data[i], data[j] = data[j], data[i]
        j += 1
    i = j

result = [str(x[1]) for x in data]
print(' '.join(result))
# TLE 3