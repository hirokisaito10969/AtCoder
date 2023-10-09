N, K = map(int, input().split())
medicines = []
max_a = 0  # aの最大値を保持する変数

for _ in range(N):
    a, b = map(int, input().split())
    medicines.append((a, b))
    max_a = max(max_a, a)

min_day = 1
max_day = max_a +1  # aの最大値を探索範囲の最大値に設定

while min_day < max_day:
    mid_day = (min_day + max_day) // 2

    total = 0
    for a, b in medicines:
        if a >= mid_day:
            total += b
        if total > K:
            break

    if total <= K:
        max_day = mid_day
    else:
        min_day = mid_day + 1

print(min_day)
