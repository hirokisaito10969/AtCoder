def rotate_string(s, indices):
    n = len(s)
    rotated = list(s)
    for i in range(len(indices)):
        color_indices = [j for j in range(n) if indices[j] == i + 1]
        if len(color_indices) > 1:
            temp = rotated[color_indices[-1]]
            for j in range(len(color_indices) - 1, 0, -1):
                rotated[color_indices[j]] = rotated[color_indices[j - 1]]
            rotated[color_indices[0]] = temp
    return ''.join(rotated)

# 入力の読み込み
N, M = map(int, input().split())
S = input().strip()
C = list(map(int, input().split()))

# 回転操作を行った後の文字列を求める
result = rotate_string(S, C)

# 結果を出力
print(result)

# 26 TLE