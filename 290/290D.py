# T = int(input())

# list = []
# for _ in range(T):
#     N, D, K = map(int, input().split())
    
#     # 印がついたマスの区間を求める
#     intervals = []
#     i = 0
#     while i < N:
#         j = i + 1
#         while (j < N) and ((j + D) % N) != i:
#             j += 1
#         intervals.append(j - i)
#         i = j

#     # K番目の印のついたマスを求める
#     total = 0
#     for i, length in enumerate(intervals):
#         total += length
#         if total >= K:
#             index = i
#             offset = length - (total - K)
#             break

#     # 答えを出力する
#     list.append((index * D + offset) % N)
#     # print((index * D + offset) % N)

# for i in range(len(list)):
#     print(str(list[i]))

import math

list = []
t = int(input())
for _ in range(t):
    n, d, k = map(int, input().split())
    k -= 1
    a = n // math.gcd(n, d)
    # print((d * k % n + k // a) % n)
    list.append((d * k % n + k // a) % n)

for i in range(len(list)):
    print(str(list[i]))
    