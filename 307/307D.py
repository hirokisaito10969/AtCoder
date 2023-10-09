def remove_parentheses(S):
    if not S:
        return ""
    
    while True:
        modified = False
        i = 0
        while i < len(S):
            if S[i] == '(' and S[i+1:].find(')') != -1:
                j = i+1+S[i+1:].find(')')
                inner_text = S[i+1:j]  # ()の内側の文字列を取得
                if '(' not in inner_text:  # ()の内側に(が含まれていない場合のみ削除
                    S = S[:i] + S[j+1:]
                    modified = True
            i += 1
        if not modified:
            break
    return S


# 入力の読み込み
N = int(input())
S = input()

# 結果の出力
result = remove_parentheses(S)
if result:
    print(result)
