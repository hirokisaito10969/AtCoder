from fractions import Fraction

N = int(input())
data = []

for i in range(1, N + 1):
    A, B = map(int, input().split())
    success_rate = A / (A + B)
    data.append((success_rate, i))

data.sort(key=lambda x: -x[0])  # 成功率の降順にソート

result = [str(x[1]) for x in data]

# 成功率が等しい場合にFractionを使用して再比較
i = 0
while i < N - 1:
    j = i + 1
    while j < N and data[j][0] == data[i][0]:
        fraction_i = Fraction(data[i][0]).limit_denominator()
        fraction_j = Fraction(data[j][0]).limit_denominator()
        if fraction_j > fraction_i:
            result[i], result[j] = result[j], result[i]
        j += 1
    i = j

print(' '.join(result))

# TLE 4