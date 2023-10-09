def find_directed_cycle(N, A):
    graph = {i + 1: A[i] for i in range(N)}

    def dfs(node, visited, cycle):
        if node in visited:
            return cycle[visited[node]:]
        visited[node] = len(cycle)
        cycle.append(node)
        next_node = graph[node]
        return dfs(next_node, visited, cycle)

    for node in range(1, N + 1):
        if node not in graph:
            continue
        cycle = dfs(node, {}, [])
        if cycle:
            return cycle

N = int(input())
A = list(map(int, input().split()))

cycle = find_directed_cycle(N, A)
print(len(cycle))
print(*cycle)
