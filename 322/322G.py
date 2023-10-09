MOD = 998244353

def solve(N, X):
    ans = 0
    
    # a と b の値を 1 から N まで試す
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a == b:
                continue
            
            # k >= 1 の条件から、S の長さは 1 以上
            for k in range(1, min(10, a, b)+1):
                f_a = (pow(a, k, MOD) - 1) * pow(a - 1, N - k, MOD) % MOD
                f_b = (pow(b, k, MOD) - 1) * pow(b - 1, N - k, MOD) % MOD
                
                if (f_a - f_b) % MOD == X:
                    ans += 1
    
    return ans % MOD

# 入力を受け取る
N, X = map(int, input().split())

# 解を計算して出力する
result = solve(N, X)
print(result)
