M = int(input())
D = list(map(int, input().split()))
total_days = sum(D)
middle_day = (total_days + 1) // 2

current_month = 1
current_day = 1
for i in range(M):
    if current_day + D[i] > middle_day:
        break
    current_month += 1
    current_day += D[i]

print(current_month, middle_day - current_day + 1)
