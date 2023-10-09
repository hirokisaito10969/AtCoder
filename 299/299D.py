# N, S = input(), input()

# l = 1
# r = N
# # while True:
# for i in range(20):
#     # 中央の位置を求める
#     m = (l + r) // 2

#     # 中央の文字列の値を尋ねる
#     print("? {}".format(m), flush=True)
#     s = int(input().strip())

#     # # 分割点が見つかった場合、その位置を返す
#     # if s == 0:
#     #     # 0のグループを探索する
#     #     r = m
#     # else:
#     #     # 1のグループを探索する
#     #     l = m
    
#     # 分割点が見つかった場合、その位置を返す
#     if s == 0:
#         # 0のグループを探索する
#         l = m
#     else:
#         # 1のグループを探索する
#         r = m

#     # 分割点が見つかった場合、
#     if l + 1 == r:
#         print("! {}".format(l), flush=True)
#         break

# exit()

# 答え
# N = int(input())
# zero = 1
# one = N

# while one - zero > 1:
#     mid = (zero + one) // 2
#     print('?', mid)
#     ans = int(input())
#     if ans == 1:
#         one = mid
#     elif ans == 0:
#         zero = mid

# print('!', zero)


N= int(input())
l = 1
r = N
while r-l > 1:
    # 中央の位置を求める
    m = (l + r) // 2

    # 中央の文字列の値を尋ねる
    print("? {}".format(m), flush=True)
    s = int(input())
    
    # 分割点が見つかった場合、その位置を返す
    if s == 0:
        # 0のグループを探索する
        l = m
    else:
        # 1のグループを探索する
        r = m

    # 分割点が見つかった場合、
    
print("! {}".format(l), flush=True)

exit()