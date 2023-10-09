import math
from collections import deque

# 入力を受け取る
N, D = map(int, input().split())
coordinates = []
for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

# ウイルス感染の判定を行う関数
def is_infected(p1, p2):
    distance_squared = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    return distance_squared <= D**2

# ウイルス感染の状態を保存するリスト
infection_status = ["No"] * N

# 人1から順に他の人との距離を判定し、ウイルス感染の状態を更新する
queue = deque([0])
infection_status[0] = "Yes"

while queue:
    i = queue.popleft()
    for j in range(N):
        if i != j and infection_status[j] == "No" and is_infected(coordinates[i], coordinates[j]):
            infection_status[j] = "Yes"
            queue.append(j)

# ウイルス感染の状態を出力する
for status in infection_status:
    print(status)
