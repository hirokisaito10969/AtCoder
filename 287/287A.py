n = int(input())
opinions = [input() for _ in range(n)]
yes_count = opinions.count("For")
if yes_count > n // 2:
    print("Yes")
else:
    print("No")
