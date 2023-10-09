N, S = input(), input()
print(max(map(len, S.split('-'))) if 'o' in S and '-' in S else -1)
# res = map(lambda len: len, S.split('-'))
# res2 = map(len, S.split('-'))
# print(list(res))
# print(list(res2))

# res = map(len,"aaddaa".split("d"))
# res = map(lambda x:x + "b","aaddaa".split("d"))
# res = map(lambda x:len(x),"aaddaa".split("d"))
# res2 = max(res)
# print(res2)
# res = map(print,"aaddaa".split("d"))
# print(list(res))

# list = [0 , 1]
# len(list)

