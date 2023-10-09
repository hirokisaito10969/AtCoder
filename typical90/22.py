A, B, C = map(int, input().split())

# 最も長い辺を基準に他の2つの辺を切り詰める回数を計算
cut1 = max(A, B, C) - A + max(A, B, C) - B + max(A, B, C) - C

# 残った2つの辺を等しい長さにするために切り詰める回数を計算
cut2 = abs(A - B) + abs(B - C) + abs(C - A)

# 切断の回数の合計を求める
total_cuts = cut1 + cut2

print(total_cuts)

# NG