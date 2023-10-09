# N, M, D = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# max_value = -1

# for i in range(N):
#     for j in range(M):
#         if abs(A[i] - B[j]) <= D:
#             total_value = A[i] + B[j]
#             max_value = max(max_value, total_value)

# print(max_value)

from bisect import bisect_right

N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

max_value = -1

for i in range(N):
    j = bisect_right(B, A[i] + D) - 1
    if (A[i]-B[j]<=D):
        if j >= 0:
            total_value = A[i] + B[j]
            max_value = max(max_value, total_value)

print(max_value)
