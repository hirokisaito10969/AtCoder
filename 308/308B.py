# 入力を受け取る
N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))

# 価格の合計を初期化
total_price = 0

# 各皿の価格を計算して合計に加える
for i in range(N):
    dish_color = C[i]
    if dish_color in D:
        total_price += P[D.index(dish_color) + 1]
    else:
        total_price += P[0]
        
    # dish_price = P[D.index(dish_color)] if dish_color in D else P[0]
    # total_price += dish_price

# 価格の合計を出力
print(total_price)
