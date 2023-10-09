def rotate_string(s, indices):
    n = len(s)
    rotated = list(s)
    # 各インデックスに対する操作を集約
    operations = {}

    for i, idx in enumerate(indices):
        if idx not in operations:
            operations[idx] = []
        operations[idx].append(i)

    for idx_list in operations.values():
        if len(idx_list) > 1:
            temp = rotated[idx_list[-1]]
            for j in range(len(idx_list) - 1, 0, -1):
                rotated[idx_list[j]] = rotated[idx_list[j - 1]]
            rotated[idx_list[0]] = temp

    return ''.join(rotated)

N, M = map(int, input().split())
S = input().strip()
C = list(map(int, input().split()))

result = rotate_string(S, C)
print(result)

# AC