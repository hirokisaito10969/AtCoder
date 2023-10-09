from collections import deque

def find_max_ball_types(N, graph):
    max_ball_types = []
    visited = [False] * (N+1)

    for v in range(2, N+1):
        queue = deque([(1, [graph[1][0][0], graph[1][0][1]])])
        visited[1] = True
        ball_types = set([graph[1][0][0], graph[1][0][1]])

        while queue:
            node, balls = queue.popleft()

            if node == v:
                max_ball_types.append(len(ball_types))
                break

            for neighbor, ball in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, balls + [ball]))
                    ball_types.add(ball)

    return max_ball_types

# 入力
N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append((V, input()))
    graph[V].append((U, input()))

# 問題を解く
result = find_max_ball_types(N, graph)

# 結果を出力
print(' '.join(map(str, result)))
