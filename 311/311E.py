def main():
    H, W, N = map(int, input().split())

    # Create a set of hole coordinates
    holes = set(tuple(map(int, input().split())) for _ in range(N))

    # Initialize the DP table with zeros
    dp = [[0] * (W + 1) for _ in range(H + 1)]

    # Calculate the number of non-hole squares for each cell (i, j)
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            dp[i][j] = (i-1) * W + j - (i * j - len(holes))

    # Count the number of non-hole squares for each hole (x, y)
    for x, y in holes:
        for dx in range(3):
            for dy in range(3):
                nx, ny = x + dx - 1, y + dy - 1
                if 1 <= nx <= H and 1 <= ny <= W:
                    dp[nx][ny] -= 1

    # Calculate the answer
    ans = sum(dp[i][j] for i in range(1, H + 1) for j in range(1, W + 1))

    print(ans)


if __name__ == "__main__":
    main()
