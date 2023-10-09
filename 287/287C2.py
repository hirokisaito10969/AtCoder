# 公式の解答。スピードが速い

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

if m != n - 1:
    print("No")
    exit()

for i in range(n):
    if len(graph[i]) > 2:
        print("No")
        exit()

reach = [False] * n
que = deque()
reach[0] = True
que.append(0)
while que:
    u = que.popleft()
    for v in graph[u]:
        if not reach[v]:
            reach[v] = True
            que.append(v)

if all(reach):
    print("Yes")
else:
    print("No")
