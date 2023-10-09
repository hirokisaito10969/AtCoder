from collections import deque, defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

if n - 1 != m:
    print("No")
    exit()

queue = deque([1])
seen = set([1])
maps = defaultdict(set)
degree = defaultdict(int)

while queue:
    v = queue.popleft()
    count = 0
    for node in graph[v]:
        count += 1
        if node in maps[v]:
            continue
        maps[node].add(v)
        if node in seen:
            print("No")
            exit()
        seen.add(node)
        queue.append(node)
    if count > 2:
        print("No")
        exit()

if len(seen) == n:
    print("Yes")
else:
    print("No")
