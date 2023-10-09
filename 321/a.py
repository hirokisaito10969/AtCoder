def is_321_like(num):
    str_num = str(num)
    for i in range(len(str_num) - 1):
        if str_num[i] <= str_num[i + 1]:
            return False

def find_321_like_rank(num):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    str_num = str(num)
    rank = 0

    for i in range(len(str_num)):
        for j in range(int(str_num[i])):
            if is_321_like(int(str_num[:i] + str(j) + str(9)*(len(str_num)-i-1))):
                rank += factorial(len(str_num)-i-1)

    return rank + 1

# 例: 9876543210 が何番目の 321-like number かを求める
num = 9876543210
rank = find_321_like_rank(num)
print(rank)
