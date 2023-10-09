import math

# 入力を受け取る
N, D = map(int, input().split())
coordinates = []
for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

# ウイルス感染の判定を行う関数
def is_infected(p1, p2):
    distance = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return distance <= D

# ウイルス感染の状態を保存するリスト
infection_status = ["No"] * N

infection_status[0] = "Yes"

# 人1から順に他の人との距離を判定し、ウイルス感染の状態を更新する
a = True

while(a):
    b = infection_status.count("Yes")
    for i in range(N):
        for j in range(N):
            if(i!=j):
                if is_infected(coordinates[i], coordinates[j]):
                    if(infection_status[i] == "Yes" or infection_status[j] == "Yes"):
                        infection_status[j] = "Yes"
                        infection_status[i] = "Yes"
    if(b == infection_status.count("Yes")):
        break
    

# ウイルス感染の状態を出力する
for status in infection_status:
    print(status)
