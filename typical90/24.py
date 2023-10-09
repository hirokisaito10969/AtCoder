N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff_sum = 0
for i in range(N):
    diff_sum += abs(A[i] - B[i])

output = "Yes" if K >= diff_sum and (K - diff_sum) % 2 == 0 else "No"
print(output)

# OK