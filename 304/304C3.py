import math

# Union-Findの実装
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root == y_root:
            return
        
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

# 入力を受け取る
N, D = map(int, input().split())
coordinates = []
for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

# ウイルス感染の状態を保存するリスト
infection_status = ["No"] * N

# ウイルス感染の判定を行う関数
def is_infected(p1, p2):
    distance_squared = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    return distance_squared <= D**2

# Union-Findを初期化
uf = UnionFind(N)
infection_status[0] = "Yes"

# 人1から順に他の人との距離を判定し、ウイルス感染の状態を更新する
for i in range(N):
    for j in range(i + 1, N):
        if is_infected(coordinates[i], coordinates[j]):
            uf.union(i, j)

# ウイルス感染の状態を出力する
for i in range(N):
    if uf.find(i) == uf.find(0):
        infection_status[i] = "Yes"

for status in infection_status:
    print(status)
