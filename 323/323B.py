N = int(input().strip())

results = []
for _ in range(N):
    results.append(input().strip())

win_counts = [0] * N

for i in range(N):
    for j in range(N):
        if i != j:
            if results[i][j] == 'o':
                win_counts[i] += 1
            elif results[i][j] == 'x':
                win_counts[j] += 1

player_scores = list(zip(range(1, N+1), win_counts))

sorted_players = sorted(player_scores, key=lambda x: x[1], reverse=True)
sorted_player_numbers = [player[0] for player in sorted_players]

print(*sorted_player_numbers)
