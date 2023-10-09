n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
mex = 0
cnt = 0
for i in range(n):
    if a[i] == mex:
        mex += 1
        cnt += 1
    if cnt == k:
        break
print(mex)
