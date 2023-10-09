# def count_characters(string):
#     count = {}
#     for char in string:
#         if char in count:
#             count[char] += 1
#         else:
#             count[char] = 1
#     return count


# # 入力を受け取る
# S = input()
# T = input()

# s = count_characters(S)
# t = count_characters(T)

# ans = "Yes"

# for char, count in s.items():
#     if s[char] == t[char]:
#         a = s[char]
#     elif t[char] == 1:
#         ans = "No"
#     elif s[char] == 1:
#         ans = "No"
        
# print(ans)



# def count_characters(string):
#     count = {}
#     for char in string:
#         if char in count:
#             count[char] += 1
#         else:
#             count[char] = 1
#     return count


# # 入力を受け取る
# S = input()
# T = input()

# s = count_characters(S)
# t = count_characters(T)

# ans = "Yes"        

# for char, count in t.items():
#     if char not in s:
#         ans = "No"
#         break
#     elif s[char] != t[char]:
#         ans = "No"
#         break
    
# print(ans)

def rle(s):
    vec = []  # 空のリストを作成
    cnt = 1  # 文字の出現回数をカウントする変数を初期化
    for i in range(1, len(s)):
        if s[i] != s[i-1]:  # 現在の文字が直前の文字と異なる場合
            vec.append((s[i-1], cnt))  # 直前の文字とその出現回数をリストに追加
            cnt = 0  # 出現回数をリセット
        cnt += 1  # 出現回数をインクリメント
    vec.append((s[-1], cnt))  # 最後の文字とその出現回数をリストに追加
    return vec

s = input()  # 文字列Sを入力
t = input()  # 文字列Tを入力

svec = rle(s)  # Sをランレングス圧縮した結果を取得
tvec = rle(t)  # Tをランレングス圧縮した結果を取得

if len(svec) != len(tvec):  # SとTの圧縮結果の長さが異なる場合
    print("No")  # Noを出力して終了
else:
    ans = True  # 結果の初期値をTrueに設定
    for i in range(len(svec)):
        if svec[i][0] != tvec[i][0]:  # 圧縮結果の文字が異なる場合
            ans = False  # 結果をFalseに設定
        if not (svec[i][1] == tvec[i][1] or (svec[i][1] < tvec[i][1] and svec[i][1] >= 2)):
            # 圧縮結果の出現回数が条件を満たさない場合
            ans = False  # 結果をFalseに設定
    if ans:
        print("Yes")  # Yesを出力
    else:
        print("No")  # Noを出力

