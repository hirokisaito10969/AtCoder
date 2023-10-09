# def can_cheat(S, T):
#     if len(S) != len(T):
#         return False
    
#     for s, t in zip(S, T):
#         if s != t and s != '@' and t != '@':
#             return False
    
#     at_count = S.count('@')
#     diff_count = sum(s != t for s, t in zip(S, T) if s != '@' and t != '@')
    
#     if at_count == 0 or diff_count == 0:
#         return True
    
#     return False

# S = input()
# T = input()

# if can_cheat(S, T):
#     print("Yes")
# else:
#     print("No")

# def can_cheat(S, T):
#     if len(S) != len(T):
#         return False
    
#     for s, t in zip(S, T):
#         if s != t and s != '@' and t != '@':
#             return False
    
#     list1 = []
#     list2 = []
#     list3 = ['a','t','c','o','d','e','r']
    
#     a = S.count('@')
#     b = T.count('@')
    
#     c = S.count('atcoder')
#     d = T.count('atcoder')
    
#     for i in range(len(S)):
#         if(S[i] != T[i]):
#             if(S[i] != '@' and T[i] != '@'):
#                 list1.append(S[i])
#                 list2.append(T[i])
                
#     if(len(S) - c <a and len(T) - d<b):
#         for i in range(len(list1)):
#             if(list3[i] not in list1 or list3[i] not in list2):
#             # if(list1 not in list3[i] or list2 not in list3[[i]]):
#                 return False
                
        
#     return True

# S = input()
# T = input()

# if can_cheat(S, T):
#     print("Yes")
# else:
#     print("No")

# def cheat_game(S, T):
    
#     a = S.count('@')
#     b = T.count('@')
    
#     c = S.count('atcoder')
#     d = T.count('atcoder')
    
#     list1 = []
#     list2 = []
    
#     for i in range(len(S)):
#         if(S[i] != T[i]):
#             if(S[i] != '@' and T[i] != '@'):
#                 list1.append(S[i])
#                 list2.append(T[i])
                
#     if(len(S) - c <a and len(T) - d<b):

#         if len(S) != len(T):
#             return "No"
        
#         for i in range(len(S)):
#             if S[i] != T[i]:
#                 if S[i] == "@":
#                     if T[i] not in ["a", "t", "c", "o", "d", "e", "r"]:
#                         return "No"
#                 elif T[i] == "@":
#                     if S[i] not in ["a", "t", "c", "o", "d", "e", "r"]:
#                         return "No"
#                 else:
#                     return "No"
    
#     return "Yes"

# # 入力の読み込み
# S = input()
# T = input()

# # 関数を呼び出して結果を出力
# result = cheat_game(S, T)
# print(result)

# from collections import Counter

# def can_win(S, T):
#     if len(S) != len(T):
#         return "No"
    
#     if S == T:
#         return "Yes"
    
#     # カードの置き換えに使用する文字のカウントを取得
#     S_count = Counter(S)
#     T_count = Counter(T)
    
#     # カードの置き換えが可能か判定
#     for i in range(7):
#         char = "@atcoder"[i]
#         if (S_count[char] + T_count[char]) > S_count["@"]:
#             return "Yes"
    
#     return "No"

# # 入力を受け取る
# S = input()
# T = input()

# # 結果を出力
# result = can_win(S, T)
# print(result)


# def cheat_game(S, T):
    
#     # a = S.count('@')
#     # b = T.count('@')
    
#     # c = S.count('atcoder')
#     # d = T.count('atcoder')
    
#     # list1 = []
#     # list2 = []
    
#     # for i in range(len(S)):
#     #     if(S[i] != T[i]):
#     #         if(S[i] != '@' and T[i] != '@'):
#     #             list1.append(S[i])
#     #             list2.append(T[i])
                
#     # if(len(S) - c <a and len(T) - d<b):

#     if len(S) != len(T):
#         return "No"
    
#     # S = sorted(S)
#     # T = sorted(T)
    
#     for i in range(len(S)):
#         if S[i] != T[i]:
#             if S[i] == "@":
#                 if T[i] not in ["a", "t", "c", "o", "d", "e", "r"]:
#                     return "No"
#             elif T[i] == "@":
#                 if S[i] not in ["a", "t", "c", "o", "d", "e", "r"]:
#                     return "No"
#             else:
#                 return "No"
        
#     return "Yes"

# # 入力の読み込み
# S = input()
# T = input()

# # 関数を呼び出して結果を出力
# result = cheat_game(S, T)
# print(result)

from collections import defaultdict
S=input()
T=input()
Scnt=defaultdict(int)
Tcnt=defaultdict(int)
for c in S: Scnt[c]+=1
for c in T: Tcnt[c]+=1

for c in "atcoder":
  M=max(Scnt[c],Tcnt[c])
  if Scnt['@']<M-Scnt[c] or Tcnt['@']<M-Tcnt[c]:
    print("No")
    exit()
  Scnt['@']-=M-Scnt[c]
  Scnt[c]=M
  Tcnt['@']-=M-Tcnt[c]
  Tcnt[c]=M

print("Yes" if Scnt==Tcnt else "No")
