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

    return dp[0]

S = input()
result = find_combinations(S)
print(result)

# 1 TLE