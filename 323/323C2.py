N, M = map(int, input().split())

point_values = list(map(int, input().split()))

player_answers = [input() for _ in range(N)]

def calculate_total_score(player,num):
    score = num + 1
    for i in range(M):
        if player[i] == 'o':
            score += point_values[i]
    return score

def calculate_total_score2(player,num):
    score = num + 1
    score_false = []
    for i in range(M):
        if player[i] == 'o':
            score += point_values[i]
        if player[i] == 'x':
            score_false.append(point_values[i])
    return score, score_false

max_score = 0
kaburi = False
for i in range(N):
    player_score = calculate_total_score(player_answers[i],i)
    if player_score > max_score:
        max_score = player_score
    elif player_score == max_score:
        kaburi = True

required_answers = [0] * N
for i in range(N):
    current_score, player_false_score = calculate_total_score2(player_answers[i],i)
    player_false_score.sort(reverse=True)
    j = 0
    while True:
        if max_score - current_score < 0:
            break
        if max_score == current_score:
            if j == 0 and kaburi:
                required_answers[i] += 1
                break
            else:
                break
        
        current_score += player_false_score[j]
        j += 1
        required_answers[i] += 1 

for ans in required_answers:
    print(ans)

# AC