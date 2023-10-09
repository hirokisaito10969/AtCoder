n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_score = sum(a[i-1] for i in b)
print(total_score)
