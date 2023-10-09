S = input()

a = S.count(S[0])
b = S.count(S[1])
c = S.count(S[2])

if(a==1):
    print(S[0])
    exit
elif(b==1):
    print(S[1])
    exit
elif(c==1):
    print(S[2])
    exit
else:
    print(-1)
    
# ChatGPT
def find_unique_character(s):
    char_count = {}

    # 文字列中の各文字の出現回数を数える
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # 出現回数が1回の文字を検索する
    for char in s:
        if char_count[char] == 1:
            return char

    return -1

# 入力を受け取る
s = input()

# 結果を出力する
result = find_unique_character(s)
print(result)
