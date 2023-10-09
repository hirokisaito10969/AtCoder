def find_kth_321_like_number(K):
    current_number = 1
    kth_number = None
    while K > 0:
        kth_number = current_number
        current_number += 1
        str_num = str(kth_number)
        is_321_like = True
        for i in range(len(str_num)-1):
            if str_num[i] <= str_num[i+1]:
                is_321_like = False
                break
        if is_321_like:
            K -= 1
    return kth_number

K = int(input())
result = find_kth_321_like_number(K)
print(result)
