W, H = map(int, input().split())
N = int(input())

strawberries = []
for _ in range(N):
    p, q = map(int, input().split())
    strawberries.append((p, q))

A = int(input())
a_values = list(map(int, input().split()))

a_values.append(H)
a_values.insert(0,0)

B = int(input())
b_values = list(map(int, input().split()))

b_values.append(W)
b_values.insert(0,0)

# 各ピースのイチゴの個数を数える
piece_strawberries = [[0] * (B+1) for _ in range(A+1)]
for i in range(len(strawberries)):
    p, q = strawberries[i]
    for i in range(len(a_values) - 1):
        if a_values[i] < p and p < a_values[i + 1]:
            for j in range(len(b_values) - 1):
                if b_values[j] < q and q < b_values[j + 1]:
                    piece_strawberries[i][j] += 1

# 最小値と最大値を計算する
min_strawberries = min([min(piece) for piece in piece_strawberries])
max_strawberries = max([max(piece) for piece in piece_strawberries])

# 結果を出力する
print(min_strawberries, max_strawberries)
