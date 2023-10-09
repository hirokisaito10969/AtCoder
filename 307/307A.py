N = int(input())
A = list(map(int, input().split()))

B = []
total_steps = 0

for i in range(N):
    weekly_steps = sum(A[i*7 : i*7 + 7])
    total_steps += weekly_steps
    B.append(weekly_steps)

for b in B:
    print(b, end=" ")
