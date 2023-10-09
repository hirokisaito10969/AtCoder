def find_abc_position(N, S):
    for n in range(N-2):
        if S[n:n+3] == "ABC":
            return n+1
    return -1

N = int(input())
S = input()

result = find_abc_position(N, S)
print(result)
