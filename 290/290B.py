n, k = map(int, input().split())
s = input()

cnt = s[:k].count("o")
pass_indexes = []
for i in range(k):
    if s[i] == "o":
        pass_indexes.append(i)

i = k
while cnt < k and i < n:
    if s[i] == "o":
        cnt += 1
        pass_indexes.append(i)
    i += 1

ans = ""
for i in range(n):
    if i in pass_indexes:
        ans += "o"
    else:
        ans += "x"
print(ans)
