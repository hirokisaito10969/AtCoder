def min_cost_to_achieve_goal(N, K, P, C, A):
    dp = [float('inf')] * (K+1)
    dp[0] = 0
    
    for i in range(N):
        for j in range(K, -1, -1):
            for k in range(1, K+1):
                if j + k <= K:
                    dp[j+k] = min(dp[j+k], dp[j] + C[i])
    
    return dp[P] if dp[P] != float('inf') else -1

# 入力を受け取る
N, K, P = map(int, input().split())
C = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

# 関数を呼び出して結果を出力
result = min_cost_to_achieve_goal(N, K, P, C, A)
print(result)
