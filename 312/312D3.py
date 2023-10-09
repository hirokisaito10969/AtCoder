MOD = 998244353

def find_combinations(S):
    N = len(S)
    dp = [0] * (N + 1)
    dp[0] = 1
    open_count = 0

    for i in range(N):
        new_dp = [0] * (N + 1)
        for j in range(open_count + 1):
            if S[i] == '(':
                new_dp[j + 1] += dp[j]
                new_dp[j + 1] %= MOD
            elif S[i] == ')':
                if j > 0:
                    new_dp[j - 1] += dp[j]
                    new_dp[j - 1] %= MOD
            else:  # S[i] == '?'
                new_dp[j + 1] += dp[j]
                new_dp[j + 1] %= MOD
                if j > 0:
                    new_dp[j - 1] += dp[j]
                    new_dp[j - 1] %= MOD
        dp = new_dp
        if S[i] == '(':
            open_count += 1
        elif S[i] == ')':
            open_count = max(open_count - 1, 0)
        else:  # S[i] == '?'
            open_count += 1

    # 逆元を計算
    inv_mod = pow(dp[N // 2], MOD - 2, MOD)
    result = (dp[0] * inv_mod) % MOD

    return result

S = input()
result = find_combinations(S)
print(result)
