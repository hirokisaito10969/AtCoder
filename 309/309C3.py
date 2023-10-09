N, K = map(int, input().split())
medicines = []

for _ in range(N):
    a, b = map(int, input().split())
    medicines.append((a, b))

min_day = 1
max_day = 10**9 + 1

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

# 自分。二部探索。不正解