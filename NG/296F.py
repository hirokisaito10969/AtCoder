N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A と B の数字の出現回数をカウントする
countA = [0] * N
countB = [0] * N
for i in range(N):
    countA[A[i]-1] += 1
    countB[B[i]-1] += 1

# A と B で異なる数字がある場合は絶対に一致しない
if sorted(A) != sorted(B):
    print("No")
else:
    # A と B が完全に一致している場合
    if all(countA[i] == countB[i] for i in range(N)):
        print("Yes")
    else:
        # A と B の数字の出現回数が異なる場合は、操作で一致させることができない
        print("No")
