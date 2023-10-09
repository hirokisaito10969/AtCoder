A, B = map(int, input().split())

# AとBの位置を特定
coordinates = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]
x1, y1 = coordinates[A - 1]
x2, y2 = coordinates[B - 1]

# AとBが同じ行に存在し、隣り合っているかどうかを判定
if y1 == y2 and abs(x1 - x2) == 1:
    print("Yes")
else:
    print("No")
