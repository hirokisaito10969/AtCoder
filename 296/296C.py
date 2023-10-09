n, x = map(int, input().split())
a = list(map(int, input().split()))

# setを使って、値の重複を削除する
a_set = set(a)

# すべての i について、A_i - X が a_set に存在するかを調べる
for i in range(n):
    if a[i] - x in a_set:
        print("Yes")
        break
else:
    print("No")
