def solve(N, M, roads):
    city_roads = [[] for _ in range(N+1)]
    for A, B, C in roads:
        city_roads[A].append((B, C))
        city_roads[B].append((A, C))
    
    dp = [[-1] * (N+1) for _ in range(1 << N)]
    
    def dfs(mask, city):
        if dp[mask][city] != -1:
            return dp[mask][city]
        
        max_length = 0
        for next_city, length in city_roads[city]:
            if mask & (1 << (next_city - 1)) == 0:
                new_mask = mask | (1 << (next_city - 1))
                max_length = max(max_length, length + dfs(new_mask, next_city))
        
        dp[mask][city] = max_length
        return max_length
    
    result = 0
    for start_city in range(1, N+1):
        start_mask = 1 << (start_city - 1)
        result = max(result, dfs(start_mask, start_city))
    
    return result

N, M = map(int, input().split())
roads = []
for _ in range(M):
    A, B, C = map(int, input().split())
    roads.append((A, B, C))

result = solve(N, M, roads)
print(result)

# AC