S = input().strip()

for i in range(2, 17, 2):
    if S[i - 1] != '0':
        print("No")
        break
else:
    print("Yes")
