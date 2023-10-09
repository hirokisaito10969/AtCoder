def is_321_like(num):
    str_num = str(num)
    for i in range(len(str_num) - 1):
        if str_num[i] <= str_num[i + 1]:
            return False
    return True

def find_kth_321_like_number(K):
    block_size = 1000
    current_block = 0
    while True:
        start = current_block * block_size + 1
        end = (current_block + 1) * block_size
        for num in range(start, end + 1):
            if is_321_like(num):
                K -= 1
                if K == 0:
                    return num
        current_block += 1

K = int(input())
result = find_kth_321_like_number(K)
print(result)

# AC 26 TLE 7