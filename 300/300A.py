n, a, b = map(int, input().split())
choices = list(map(int, input().split()))

for i, c in enumerate(choices):
    if c == a + b:
        print(i + 1)
        break
