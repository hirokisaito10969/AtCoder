def apply_operations(S, operations):
    result = list(S)
    for op in operations:
        t = op[0]
        if t == 1:
            x, c = op[1], op[2]
            result[x - 1] = c
        elif t == 2:
            result = [char.lower() for char in result]
        elif t == 3:
            result = [char.upper() for char in result]
    return ''.join(result)

# 入力の読み込み
N = int(input())
S = input().strip()
Q = int(input())
operations = []
for _ in range(Q):
    t, x, c = input().split()
    t = int(t)
    x = int(x) if t == 1 else 0
    operations.append((t, x, c))

# 操作を適用して結果を出力
result = apply_operations(S, operations)
print(result)

# 18 TLE