N, K = map(int, input().split())

p = []
for _ in range(N):
    a, b = map(int, input().split())
    p.append((a, b))

p.sort()

total = sum(b for a, b in p)

if total <= K:
    print(1)
else:
    for i in range(N):
        if total <= K:
            print(p[i-1][0] + 1)
            break
        total -= p[i][1]
    else:
        print(p[-1][0] + 1)

# 解説。正解。
