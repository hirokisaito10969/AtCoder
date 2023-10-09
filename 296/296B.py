# 8行の入力を受け取る
S = [input() for _ in range(8)]

# "*" の位置を特定する
for i in range(8):
    if "*" in S[i]:
        j = S[i].index("*")
        break

# 対応するマスの名前を求める
row = 8 - i
col = chr(ord("a") + j)
ans = col + str(row)

# 結果を出力する
print(ans)
