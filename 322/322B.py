N, M = map(int, input().split())
S = input()
T = input()

if S == T[:N] and S == T[-N:]:
    result = 0
elif S == T[:N]:
    result = 1
elif S == T[-N:]:
    result = 2
else:
    result = 3

print(result)
