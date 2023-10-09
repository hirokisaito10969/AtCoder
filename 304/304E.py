from collections import defaultdict, deque

def is_good_graph(graph, N, forbidden_paths):
    visited = [False] * (N + 1)

    for forbidden_path in forbidden_paths:
        start, end = forbidden_path
        if has_path(graph, start, end, visited):
            return False

    return True

def has_path(graph, start, end, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return False

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

# グラフの情報を入力
N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 良いグラフかどうかを判定
K = int(input())
forbidden_paths = []
for _ in range(K):
    x, y = map(int, input().split())
    forbidden_paths.append((x, y))

# Q個の質問に回答
Q = int(input())
for _ in range(Q):
    p, q = map(int, input().split())
    # 辺を追加した新しいグラフを作成
    add_edge(graph, p, q)
    # 良いグラフかどうかを判定
    if is_good_graph(graph, N, forbidden_paths):
        print("Yes")
    else:
        print("No")
