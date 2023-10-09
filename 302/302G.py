# N = int(input())
# A = list(map(int, input().split()))

# swap_count = 0

# for i in range(N - 1):
#     if A[i] > A[i + 1]:
#         min_val = min(A[i + 1:])
#         min_index = A.index(min_val, i + 1)
#         A[i], A[min_index] = A[min_index], A[i]
#         swap_count += 1
#         i -= 1

# print(swap_count)

N = int(input())
A = list(map(int, input().split()))

swap_count = 0

def find_minimum_above(array, target_value):
    min_value = float('inf')  # 初期値として無限大を設定

    for num in array:
        if num > target_value and num < min_value:
            min_value = num

    return min_value

temp = 0
for i in range(N - 1):
    # if A[i] > A[i + 1]:
    a = A.index(find_minimum_above(A, temp))
    if i < a:
        tmp = A[a]
        A[a] = A[i]
        A[i] = tmp
        swap_count += 1
        # i -= 1

print(swap_count)
