def check_sheet(A, B, X):
    # シートXのサイズ
    HX, WX = len(X), len(X[0])

    # シートAとシートBに含まれる黒いマスの座標を集める
    black_A = set()
    black_B = set()
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == '#':
                black_A.add((i, j))
    for i in range(len(B)):
        for j in range(len(B[0])):
            if B[i][j] == '#':
                black_B.add((i, j))

    # シートCから切り出す領域を全て試す
    for i in range(len(A) - HX + 1):
        for j in range(len(A[0]) - WX + 1):
            # 切り出された領域
            cut_sheet = []
            for k in range(HX):
                cut_sheet.append(A[i+k][j:j+WX])

            # 切り出された領域に含まれる黒いマスの座標を集める
            black_cut = set()
            for k in range(HX):
                for l in range(WX):
                    if cut_sheet[k][l] == '#':
                        black_cut.add((k, l))

            # シートAの黒いマスと切り出された領域の黒いマスを比較し、一致するかチェックする
            if black_A.issubset(black_cut):
                # シートBの黒いマスが重なっていても問題ないので、シートBの黒いマスを無視してシートXと比較する
                for k in range(HX):
                    for l in range(WX):
                        if X[k][l] == '#' and (k, l) not in black_cut:
                            return False
                return True

    return False

# 入力の読み込み
HA, WA = map(int, input().split())
A = [input() for _ in range(HA)]
HB, WB = map(int, input().split())
B = [input() for _ in range(HB)]
HX, WX = map(int, input().split())
X = [input() for _ in range(HX)]

# 結果の出力
if check_sheet(A, B, X):
    print("Yes")
else:
    print("No")
