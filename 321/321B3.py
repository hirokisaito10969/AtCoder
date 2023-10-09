def calculate_min_score(N, X, scores):
    total_scores = sum(scores)
    scores.sort()
    
    scoresa = scores
    scoresb = scores
    
    if total_scores - scoresa[-1] >= X:
        scoresa.append(0)
        scoresa.sort()
        scoresa = scoresa[1:-1]
        if sum(scoresa) > X:
            return 0
    
    if total_scores - scoresb[0] < X:
        scoresb.append(100)
        scoresb.sort()
        scoresb = scoresb[1:-1]
        if sum(scoresb) < X:
            return -1
    
    scores = scores[1:-1]
    total_scores = sum(scores)
    required_score = X - total_scores
    
    return required_score

N, X = map(int, input().split())
scores = list(map(int, input().split()))

result = calculate_min_score(N, X, scores)
print(result)

# AC