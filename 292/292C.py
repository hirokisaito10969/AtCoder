# N = int(input())
# count = 0
# for A in range(1, N):
#     for B in range(1, N):
#         count_AB = A * B
#         if(count_AB < N):
#             for C in range(1, N):
#                 if(count_AB + C < N):
#                     for D in range(1, N):
#                         count_CD = C * D                    
#                         if(count_AB + count_CD == N):
#                             count += 1
# print(count)

# import itertools
# N=int(input())
# list = list(itertools.product(range(1, N), repeat=4))
# count=0
# for A,B,C,D in list:
#     if(A*B+C*D==N):
#         count+=1
# print(count)

# N = int(input())
# count = 0
# for A in range(1, N):
#     for B in range(1, N):
#         count_AB = A * B
#         if count_AB >= N:
#             break
#         for C in range(1, N):
#             if count_AB + C >= N:
#                 break
#             for D in range(1, N):
#                 count_CD = C * D                    
#                 if count_AB + count_CD == N:
#                     count += 1
#                     break
# print(count)

import math

N = int(input())

ans = 0

for i in range(1, N):
    X, Y = i, N - i
    x, y = 0, 0
    sqrtX = int(math.sqrt(X))
    sqrtY = int(math.sqrt(Y))
    for j in range(1, sqrtX + 1):
        if X % j == 0:
            x += 1
            if X != j * j:
                x += 1
    for j in range(1, sqrtY + 1):
        if Y % j == 0:
            y += 1
            if Y != j * j:
                y += 1
    ans += x * y

print(ans)
