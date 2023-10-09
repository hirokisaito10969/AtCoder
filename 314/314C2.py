def optimized_rotate_string(s, indices):
    n = len(s)
    rotated = list(s)
    rotation_count = [0] * n
    
    # 各インデックスに対する回転操作回数を数える
    for index in indices:
        rotation_count[index - 1] += 1
    
    # 回転操作をまとめて行う
    for i in range(n):
        if rotation_count[i] > 0:
            shift = rotation_count[i] % n
            rotated[i:] = rotated[i + shift:] + rotated[i:i + shift]
    
    return ''.join(rotated)

# 入力の読み込み
N, M = map(int, input().split())
S = input().strip()
C = list(map(int, input().split()))

# 回転操作を行った後の文字列を求める
result = optimized_rotate_string(S, C)

# 結果を出力
print(result)

# WA