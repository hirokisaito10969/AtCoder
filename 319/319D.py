def can_fit(words, W, M):
    lines = 1
    current_width = 0

    for word in words:
        if current_width + word > W:
            lines += 1
            current_width = word
        else:
            current_width += word

    return lines <= M

def minimum_width(N, M, L):
    left = 1
    right = sum(L)

    while left < right:
        mid = (left + right) // 2
        if can_fit(L, mid, M):
            right = mid
        else:
            left = mid + 1

    return left

# 入力例1
N1, M1, L1 = 13, 3, [9, 5, 2, 7, 1, 8, 8, 2, 1, 5, 2, 3, 6]
result1 = minimum_width(N1, M1, L1)
print(result1)  # Output: 26

# 入力例2
N2, M2, L2 = 10, 1, [1000000000] * 10
result2 = minimum_width(N2, M2, L2)
print(result2)  # Output: 10000000009

# 入力例3
N3, M3, L3 = 30, 8, [8, 55, 26, 97, 48, 37, 47, 35, 55, 5, 17, 62, 2, 60, 23, 99, 73, 34, 75, 7, 46, 82, 84, 29, 41, 32, 31, 52, 32, 60]
result3 = minimum_width(N3, M3, L3)
print(result3)  # Output: 189
