import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A, B を list に変換する
A = list(A)
B = list(B)

# C を作成
C = A + B
C.sort()

# A, B が C の何番目にあるか調べる
A_pos = [bisect.bisect_left(C, a) + 1 for a in A]
B_pos = [bisect.bisect_left(C, b) + 1 for b in B]

# 結果を出力
print(*A_pos)
print(*B_pos)
