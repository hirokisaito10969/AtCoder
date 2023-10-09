# mod = 998244353
# S = "1"

# Q = int(input())

# queries = []
# for i in range(Q):
#     queries.append(input().split())

# cnt = 0
# for query in queries:
#     if query[0] == "1":
#         S += query[1]
#     elif query[0] == "2":
#         S = S[1:]
#     else:
#         cnt += 1
#         val = int(S) % mod
#         print(val)


mod = 998244353
S = "1"
Q = int(input())

for i in range(Q):
    query = input().split()
    if query[0] == "1":
        S += query[1]
    elif query[0] == "2":
        S = S[1:]
    else:
        val = int(S) % mod
        print(val)


# mod = 998244353

# Q = int(input())

# S = 1
# val = 1
# cnt = 1

# list1 = []
# for i in range(Q):
#     query = input().split()
#     if query[0] == "1":
#         val = val * 10 + int(query[1])
#         cnt += 1
#     elif query[0] == "2":
#         cnt -= 1
#         # S = int(val / (10 ** cnt))
#         # val = val - S * 10 ** cnt
#         S = int(val / (pow(10, cnt)))
#         val = val - S * (pow(10, cnt))
#     else:
#         val = val % mod
#         print(val)


# import sys
# from collections import deque

# input = sys.stdin.readline
# mod = 998244353

# S = deque([1])
# Q = int(input())

# digit_values = [1] * (10 ** 6 + 1)
# for i in range(1, len(digit_values)):
#     digit_values[i] = (digit_values[i-1] * 10) % mod

# for i in range(Q):
#     query = input().split()
#     if query[0] == "1":
#         S.append(int(query[1]))
#     elif query[0] == "2":
#         S.popleft()
#     else:
#         val = 0
#         for j, digit in enumerate(S):
#             val += digit * digit_values[len(S) - j - 1]
#             val %= mod
#         print(val)
