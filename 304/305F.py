def count_shift_patterns(N, S):
    MOD = 998244353
    patterns = 1

    # 出勤する日数を数える
    D = 0
    for c in S:
        if c == '#':
            D += 1

    # 青木君のシフト表の個数を求める
    for i in range(1, D+1):
        if N % i == 0:
            # D日間のシフト表
            shift = S[:i]
            # 残りのN-D日間のシフト表
            remaining = S[i:]

            for j in range(N-D):
                # N-D+j日目の勤怠をi日目の勤怠と一致させる
                if shift[j % i] != remaining[j]:
                    break
            else:
                patterns = (patterns * (N // i)) % MOD

    return patterns

# シフト表の情報を入力
N = int(input())
S = input()

# 青木君のシフト表の個数を求める
result = count_shift_patterns(N, S)
print(result)
