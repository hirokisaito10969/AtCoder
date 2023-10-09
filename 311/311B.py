def max_continuous_days(n, d, schedules):
    max_continuous_days = 0
    current_continuous_days = 0

    for day in range(d):
        all_free = True
        for person in range(n):
            if schedules[person][day] == 'x':
                all_free = False
                break

        if all_free:
            current_continuous_days += 1
            max_continuous_days = max(max_continuous_days, current_continuous_days)
        else:
            current_continuous_days = 0

    return max_continuous_days

# 入力を受け取る
n, d = map(int, input().split())
schedules = []
for _ in range(n):
    schedule = input().strip()
    schedules.append(schedule)

# 結果を出力
result = max_continuous_days(n, d, schedules)
print(result)
