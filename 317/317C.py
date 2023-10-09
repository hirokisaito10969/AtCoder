def solve(N, M, roads):
    city_roads = [[] for _ in range(N+1)]
    for A, B, C in roads:
        city_roads[A].append((B, C))
        city_roads[B].append((A, C))
    
    def dfs(current_city, visited):
        if all(visited):
            return 0
        max_length = 0
        for next_city, length in city_roads[current_city]:
            if not visited[next_city]:
                visited[next_city] = True
                max_length = max(max_length, length + dfs(next_city, visited))
                visited[next_city] = False
        return max_length
    
    max_distance = 0
    for start_city in range(1, N+1):
        visited = [False] * (N+1)
        visited[start_city] = True
        max_distance = max(max_distance, dfs(start_city, visited))
    
    return max_distance

N, M = map(int, input().split())
roads = []
for _ in range(M):
    A, B, C = map(int, input().split())
    roads.append((A, B, C))

result = solve(N, M, roads)
print(result)

# TLE 6