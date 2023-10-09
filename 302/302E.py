# 入力
N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
unconnected = set(range(1, N+1))
output = []

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        u, v = query[1:]
        graph[u].append(v)
        graph[v].append(u)
        unconnected.discard(u)
        unconnected.discard(v)
    else:
        v = query[1]
        for neighbor in graph[v]:
            graph[neighbor].remove(v)
            if len(graph[neighbor]) == 0:
                unconnected.add(neighbor)
        graph[v] = []
        unconnected.add(v)
    
    output.append(len(unconnected))

# # 問題を解く

# # 結果を出力
# for count in output:
#     print(count)

# class UnionFind:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0] * n
#         self.size = [1] * n

#     def find(self, x):
#         if self.parent[x] == x:
#             return x
#         self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, x, y):
#         root_x = self.find(x)
#         root_y = self.find(y)

#         if root_x != root_y:
#             if self.rank[root_x] < self.rank[root_y]:
#                 root_x, root_y = root_y, root_x
#             self.parent[root_y] = root_x
#             self.size[root_x] += self.size[root_y]
#             if self.rank[root_x] == self.rank[root_y]:
#                 self.rank[root_x] += 1

#     def get_size(self, x):
#         root = self.find(x)
#         return self.size[root]


# def solve_queries(N, queries):
#     unconnected = N
#     uf = UnionFind(N + 1)
#     results = []

#     for query in queries:
#         q_type = query[0]

#         if q_type == 1:
#             u, v = query[1], query[2]
#             if uf.find(u) != uf.find(v):
#                 unconnected -= uf.get_size(u) + uf.get_size(v)
#                 uf.union(u, v)
#         elif q_type == 2:
#             v = query[1]
#             if uf.parent[v] == v:
#                 unconnected -= uf.get_size(v)

#         results.append(unconnected)

#     return results


# # 入力
# N, Q = map(int, input().split())
# queries = []

# for _ in range(Q):
#     query = list(map(int, input().split()))
#     queries.append(query)

# # 問題を解く
# output = solve_queries(N, queries)

# # 結果を出力
# for count in output:
#     print(count)
