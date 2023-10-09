def find_cycle(graph, start):
    visited = set()
    stack = [(start, [])]

    while stack:
        node, path = stack.pop()

        if node in visited:
            cycle_start = path.index(node)
            return path[cycle_start:]

        if node not in visited:
            visited.add(node)
            stack.extend((neighbor, path + [node]) for neighbor in graph[node])

    return None

def main():
    N = int(input())
    A = list(map(int, input().split()))

    graph = {i + 1: [A[i]] for i in range(N)}

    cycle_found = False
    for i in range(1, N + 1):
        if not cycle_found:
            cycle = find_cycle(graph, i)
            if cycle:
                cycle_found = True
                print(len(cycle))
                print(*cycle)
                break  # サイクルが見つかったら探索を終了

    # if not cycle_found:
    #     print("No cycle found.")

if __name__ == "__main__":
    main()

# 15 TLE