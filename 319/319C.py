def calculate_probability(grid):
    # dp[i][j][k][l][m][n] は i番目の数字を見た後、それぞれの行と列がどの数字であるかを表す
    dp = [[[[[[0 for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]
    
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):
                    for e in range(1, 10):
                        for f in range(1, 10):
                            if a != grid[0][0] and b != grid[0][1] and c != grid[0][2] and d != grid[1][0] and e != grid[1][1] and f != grid[1][2]:
                                dp[a][b][c][d][e][f] = 1
    
    for i in range(9, 0, -1):
        for j in range(9, 0, -1):
            for k in range(9, 0, -1):
                for l in range(9, 0, -1):
                    for m in range(9, 0, -1):
                        for n in range(9, 0, -1):
                            total = 6
                            if i == j == k:
                                total -= 1
                            if i == l == m:
                                total -= 1
                            if j == l == n:
                                total -= 1
                            if k == m == n:
                                total -= 1
                            if i == l and j == m and k == n:
                                total += 1
                            dp[i][j][k][l][m][n] /= total
                            dp[i][j][k][l][m][n] += dp[j][k][l][m][n][i] / total
                            dp[i][j][k][l][m][n] += dp[i][k][l][m][n][j] / total
                            dp[i][j][k][l][m][n] += dp[i][j][l][m][n][k] / total
                            dp[i][j][k][l][m][n] += dp[i][j][k][m][n][l] / total
                            dp[i][j][k][l][m][n] += dp[i][j][k][l][n][m] / total
    
    result = dp[1][2][3][4][5][6] + dp[1][2][3][4][6][5] + dp[1][2][3][5][4][6] + dp[1][2][3][5][6][4] + dp[1][2][3][6][4][5] + dp[1][2][3][6][5][4]
    return result

# 入力を受け取る
grid = [[int(x) for x in input().split()] for _ in range(3)]

# 確率を計算して出力
probability = calculate_probability(grid)
print(format(probability, '.15f'))
