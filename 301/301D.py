# import math

# S=input()
# T=int(input())

# a = 0
# i = 0
# while(a<T):
#     if(S[len(S)-i-1] == '?'):
#         a += math.pow(2, i)
#     else:
#         a += int(S[len(S)-i-1])
#     i+=1
#     if(i==len(S)):
#         break

# if(a>T):
#     print("-1")
# else:
#     print(a)

# import math

# S=input()
# T=int(input())

# list1 = []
# i = 0
# for i in range(len(S)):
#     if(S[i] == '?'):
#         i += math.pow(2, i)
#     else:
#         i += int(S[len(S)-i-1])

# if(i<T):
#     print("-1")
# else:
#     print(i)

S, N = list(reversed(input())), int(input())
s = 0
for i in range(len(S)):
    s |= (S[i] == '1') << i
if s > N:
    print(-1)
else:
    for i in reversed(range(len(S))):
        if S[i] == '?' and (s | 1 << i) <= N:
            s |= 1 << i
    print(s)
