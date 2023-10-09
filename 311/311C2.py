def find_cycle(graph):
    n = len(graph)
    visited = [False] * n

    def dfs(v, path):
        visited[v] = True

        for u in graph[v]:
            if u in path:
                return path[path.index(u):]
            elif not visited[u]:
                cycle = dfs(u, path + [u])
                if cycle:
                    return cycle

        return []

    for start in range(n):
        if not visited[start]:
            cycle = dfs(start, [start])
            if cycle:
                return cycle

    return []

def main():
    N = int(input())
    A = list(map(int, input().split()))

    graph = [[] for _ in range(N)]
    for i, a in enumerate(A):
        graph[i].append(a - 1)  # Convert to 0-indexed graph

    cycle = find_cycle(graph)

    M = len(cycle)
    print(M)
    print(*[vertex + 1 for vertex in cycle])  # Convert back to 1-indexed

if __name__ == "__main__":
    main()

# 18 RE