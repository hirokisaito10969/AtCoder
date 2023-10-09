from itertools import permutations

def check_conditions(strings):
    for i in range(len(strings) - 1):
        diff_count = sum(a != b for a, b in zip(strings[i], strings[i+1]))
        if diff_count != 1:
            return False
    return True

N, M = map(int, input().split())
S = [input() for _ in range(N)]

# 文字列の順列を生成し、条件を満たすかどうかをチェック
permutations_list = list(permutations(S))
for perm in permutations_list:
    if check_conditions(perm):
        print("Yes")
        exit()

print("No")
