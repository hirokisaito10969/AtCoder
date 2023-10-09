N = int(input())
students = []
for _ in range(N):
    C, P = map(int, input().split())
    students.append((C, P))

Q = int(input())
queries = []
for _ in range(Q):
    L, R = map(int, input().split())
    queries.append((L, R))

class_scores = [[0, 0] for _ in range(N+1)]  # 各クラスの得点の合計を保持するリスト

for i in range(1, N+1):
    class_scores[i][0] = class_scores[i-1][0]
    class_scores[i][1] = class_scores[i-1][1]
    if students[i-1][0] == 1:
        class_scores[i][0] += students[i-1][1]
    else:
        class_scores[i][1] += students[i-1][1]

for L, R in queries:
    score_class1 = class_scores[R][0] - class_scores[L-1][0]
    score_class2 = class_scores[R][1] - class_scores[L-1][1]
    print(score_class1, score_class2)

# OK