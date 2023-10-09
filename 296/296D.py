# import math
# N, M = map(int, input().split())
# sqrtM = int(math.sqrt(M))
# n = N*N
# if(N*N>=M):
#     for i in range(int(sqrtM),N):
#         if(i*N>=M):
#             for j in range(int(sqrtM),N):
#                 if(M<i*j and i*j<n):
#                     n = i*j
#                     break
#     print(str(n))
# else:
#     print(-1)


# import math
# N, M = map(int, input().split())
# sqrtM = int(math.sqrt(M))
# min = N*N
# count=0
# if(M<=N*N):
#     for i in range(sqrtM,N +1):
#         if(M<=sqrtM*i and i*N<=min):
#             for j in range(sqrtM,N + 1):
#                 if(M<=i*j and i*j<=min):
#                     min = i*j
#                     count +=1
#                     break
#     if(count == 0):
#         print(-1)
#     else:
#         print(str(min))
# else:
#     print(-1)

import math
N, M = map(int, input().split())

X = float('inf')  # X の初期値を無限大に設定
for a in range(1, N + 1):
    b = (M + a - 1) // a  # a*b >= M を満たす最小の b を計算
    if b <= N:  # b が N 以下である場合、X を更新
        X = min(X, a * b)
    if a > b:
        break

if X == float('inf'):  # X が更新されていない場合、-1 を出力
    print(-1)
else:
    print(X)

# import sys
# n, m = map(int, sys.stdin.readline().split())
# INF = 2 * 10**18
# ans = INF
# for i in range(1, n+1):
#     x = (m+i-1)//i
#     if x <= n:
#         ans = min(ans, i*x)
#     if i > x:
#         break
# if ans == INF:
#     print(-1)
# else:
#     print(ans)
