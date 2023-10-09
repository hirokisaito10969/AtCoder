MOD = 998244353

def find_combinations(S):
    N = len(S)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if S[i] == '(':
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= MOD
            elif S[i] == ')':
                if j > 0:
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j-1] %= MOD
            else:  # S[i] == '?'
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= MOD
                if j > 0:
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j-1] %= MOD

    return dp[N][0]

S = input()

result = find_combinations(S)
print(result)


# 13 TLE