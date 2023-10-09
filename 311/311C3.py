def find_cycle(graph, start):
    visited = set()
    stack = [start]
    path = []

    while stack:
        node = stack.pop()

        if node in path:
            cycle_start = path.index(node)
            return path[cycle_start:]

        if node not in visited:
            visited.add(node)
            path.append(node)
            stack.extend(graph[node])

    return None

def main():
    N = int(input())
    A = list(map(int, input().split()))

    graph = {i + 1: [A[i]] for i in range(N)}

    for i in range(1, N + 1):
        cycle = find_cycle(graph, i)
        if cycle:
            break

    print(len(cycle))
    print(*cycle)

if __name__ == "__main__":
    main()

# 16 TLE