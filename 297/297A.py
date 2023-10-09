N, D = map(int, input().split())
T = list(map(int, input().split()))

first_double_click = -1  # 最初のダブルクリックの時刻を格納する変数

for i in range(N-1):
    if T[i+1] - T[i] <= D:
        first_double_click = T[i+1]
        break

print(first_double_click)
