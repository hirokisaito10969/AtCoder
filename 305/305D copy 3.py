import bisect

N = int(input())
A = list(map(int, input().split()))
fA = [0] * N

# fA[i] := A[i] 分までに何分寝たか
for i in range(1, N):
    if i % 2 == 0:
        fA[i] = fA[i - 1] + A[i] - A[i - 1]
    else:
        fA[i] = fA[i - 1]

Q = int(input())

# f(x) := x 分までに何分寝たか
def f(x):
    j = bisect.bisect_right(A[1:], x) - 1
    return fA[j] + (fA[j + 1] - fA[j]) // (A[j + 1] - A[j]) * (x - A[j])

for _ in range(Q):
    l, r = map(int, input().split())
    print(f(r) - f(l))
