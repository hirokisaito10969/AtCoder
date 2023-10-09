def is_321_like(num):
    str_num = str(num)
    for i in range(len(str_num) - 1):
        if str_num[i] <= str_num[i + 1]:
            return False
    return True

def find_kth_321_like_number(K):
    current_num = 1
    while K > 0:
        if is_321_like(current_num):
            K -= 1
        current_num += 1
    return current_num - 1


K = int(input())
result = find_kth_321_like_number(K)
print(result)

# AC 26 TLE 7