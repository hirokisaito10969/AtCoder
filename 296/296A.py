n = int(input())
s = input()

# 文字列sの隣り合う2文字が同じ性別の場合、交互に並んでいないとみなす
for i in range(n-1):
    if s[i] == s[i+1]:
        print("No")
        exit()

# すべての隣り合う2文字が異なる性別の場合、交互に並んでいると判断する
print("Yes")
