def process_queries(N, Q, S, queries):
    results = []
    ones_count = S.count('1')
    
    for query in queries:
        c, L, R = query
        if c == 1:
            for i in range(L-1, R):
                if S[i] == '1':
                    ones_count -= 1
                    S = S[:i] + '0' + S[i+1:]
                else:
                    ones_count += 1
                    S = S[:i] + '1' + S[i+1:]
        else:
            T = S[L-1:R]
            max_ones = max(map(len, T.split('0')))
            results.append(max_ones)
    
    return results

N, Q = map(int, input().split())
S = input()
queries = [list(map(int, input().split())) for _ in range(Q)]

results = process_queries(N, Q, S, queries)
for result in results:
    print(result)

# 8 AC 10 TLE