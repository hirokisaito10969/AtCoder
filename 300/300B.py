import numpy as np

H, W = map(int, input().split())
A = [list(input().strip()) for _ in range(H)]
B = [list(input().strip()) for _ in range(H)]

AA = np.array(A)
BB = np.array(B)

for i in range(H):
    for j in range(W):
        if(np.array_equal(AA, np.roll(BB, (i, j), axis=(0, 1)))):
            print("Yes")
            exit()
print("No")
            