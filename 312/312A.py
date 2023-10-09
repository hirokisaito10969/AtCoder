def is_valid_string(S):
    valid_strings = ['ACE', 'BDF', 'CEG', 'DFA', 'EGB', 'FAC', 'GBD']
    return S in valid_strings

# 標準入力から文字列を取得
S = input().strip()

# 判定して結果を出力
if is_valid_string(S):
    print("Yes")
else:
    print("No")
