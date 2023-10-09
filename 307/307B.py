def is_palindrome(s):
    return s == s[::-1]

N = int(input())
S = []
for _ in range(N):
    S.append(input())

found = False

for i in range(N):
    for j in range(i+1, N):
        concat = S[i] + S[j]
        if is_palindrome(concat):
            found = True
            break

if found == False:
    for i in range(N-1, -1, -1):
        for j in range(i-1, -1, -1):
            concat = S[i] + S[j]
            if is_palindrome(concat):
                found = True
                break
        if found:
            break


if found:
    print("Yes")
else:
    print("No")
