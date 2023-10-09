import bisect

def min_slime_count(slimes):
    slimes.sort()  # サイズが小さい順にソート

    count = 0
    while len(slimes) > 1:
        smallest = slimes.pop(0)  # 一番小さいスライムを取り出す
        second_smallest = slimes.pop(0)  # 次に小さいスライムを取り出す
        new_size = smallest * 2  # 新しいスライムのサイズは2倍
        count += 1
        slimes.insert(bisect.bisect_left(slimes, new_size), new_size)  # 新しいスライムを挿入

    return count


# 入力例1
slimes_1 = [(3, 3), (5, 1), (6, 1)]
result_1 = min_slime_count([size for size, count in slimes_1])
print(result_1)  # 出力: 3

# 入力例2
slimes_2 = [(1, 1), (2, 1), (3, 1)]
result_2 = min_slime_count([size for size, count in slimes_2])
print(result_2)  # 出力: 3

# 入力例3
slime_3 = [(1000000000, 1000000000)]
result_3 = min_slime_count([size for size, count in slime_3])
print(result_3)  # 出力: 13
