def select_passing_students(N, X, Y, Z, math_scores, english_scores):
    # 合格者のリスト
    passing_students = []

    # 数学の点が高い順にX人を合格とする
    sorted_math = sorted(range(N), key=lambda i: (-math_scores[i], i))
    passing_students.extend(sorted_math[:X])

    # まだ合格していない受験者のうち、英語の点が高い順にY人を合格とする
    remaining_students = set(range(N)) - set(passing_students)
    sorted_english = sorted(remaining_students, key=lambda i: (-english_scores[i], i))
    passing_students.extend(sorted_english[:Y])

    # まだ合格していない受験者のうち、数学と英語の合計点が高い順にZ人を合格とする
    remaining_students = set(range(N)) - set(passing_students)
    sorted_total = sorted(remaining_students, key=lambda i: (-(math_scores[i] + english_scores[i]), i))
    passing_students.extend(sorted_total[:Z])

    # 合格者の番号を小さい順に出力
    passing_students.sort()
    for student in passing_students:
        print(student+1)

# 入力を受け取る
N, X, Y, Z = map(int, input().split())
math_scores = list(map(int, input().split()))
english_scores = list(map(int, input().split()))

# 処理を実行
select_passing_students(N, X, Y, Z, math_scores, english_scores)
