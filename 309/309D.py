from collections import deque

def get(E, s):
    n = len(E)
    dist = [-1] * n
    dist[s] = 0
    Q = deque([s])

    while Q:
        x = Q.popleft()
        for y in E[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                Q.append(y)

    return max(dist)

if __name__ == "__main__":
    N1, N2, M = map(int, input().split())

    E = [[] for _ in range(N1 + N2)]

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        E[a].append(b)
        E[b].append(a)

    print(get(E, 0) + get(E, N1 + N2 - 1) + 1)
