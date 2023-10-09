def find_first_occurrence(n, s):
    count_A, count_B, count_C = 0, 0, 0
    for i in range(n):
        if s[i] == 'A':
            count_A += 1
        elif s[i] == 'B':
            count_B += 1
        elif s[i] == 'C':
            count_C += 1
        
        if count_A >= 1 and count_B >= 1 and count_C >= 1:
            return i + 1  # 左から i 番目までに条件を満たす
    return n  # 条件を満たさない場合は n まで見た時点で終了

# 入力を受け取る
n = int(input())
s = input()

# 結果を出力
result = find_first_occurrence(n, s)
print(result)
