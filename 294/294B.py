H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# アルファベットのリストを生成
alphabets = [chr(i) for i in range(65, 91)]

for i in range(H):
    s = ''
    for j in range(W):
        if A[i][j] == 0:
            s += '.'
        else:
            s += alphabets[A[i][j] - 1]
    print(s)
