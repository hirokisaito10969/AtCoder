def calculate_min_score(N, X, scores):
    total_scores = sum(scores)
    min_score = min(scores)
    max_score = max(scores)
    final_result = total_scores - min_score - max_score
    
    if final_result >= X:
        return 0
    else:
        required_score = X - final_result
        if required_score <= 100:
            return required_score
        else:
            return -1

# 入力を受け取る
N, X = map(int, input().split())
scores = list(map(int, input().split()))

result = calculate_min_score(N, X, scores)
print(result)
