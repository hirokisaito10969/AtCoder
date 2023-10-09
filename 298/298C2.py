from collections import defaultdict, Counter

# n, q = map(int, input().split())
n = int(input())
q = int(input())

# 箱に入っているカードの数値を管理するための辞書
cards_in_box = defaultdict(Counter)

# 数値が書かれたカードが入っている箱の一覧を管理するための辞書
boxes_with_num = defaultdict(set)

list1 = []
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i, j = query[1], query[2]
        # カードに数値を書き込み、箱に入れる
        cards_in_box[j][i] += 1
        # 数値が書かれたカードが箱jに入っていることを記録する
        boxes_with_num[i].add(j)
    elif query[0] == 2:
        i = query[1]
        # 箱iに入っているカードに書かれた数値の一覧を昇順に出力する
        list1.append(sorted(cards_in_box[i].elements()))
        # print(*sorted(cards_in_box[i].elements()))
    else:
        i = query[1]
        # 数値iが書かれたカードが入っている箱の一覧を昇順に出力する
        # print(*sorted(boxes_with_num[i]))
        list1.append(sorted(boxes_with_num[i]))

for i in list1:
    print(*i)
