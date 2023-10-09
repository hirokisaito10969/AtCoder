# N, Q = map(int, input().split())
N = int(input())
Q = int(input())
cards = [[] for _ in range(N)]
boxes = [set() for _ in range(2 * 10**5)]
for i in range(Q):
    # query = [int(x) for x in input().split()] # リスト内包表記を使って修正
    query = list(map(int, input().split()))

    if query[0] == 1:
        cards[query[2] - 1].append(str(query[1]))
        boxes[query[1] - 1].add((query[2]))
    elif query[0] == 2:
        ans = []
        for card in cards[query[1] - 1]:
            ans += list(boxes[int(card) - 1])
        ans.sort()
        list.append(ans)
        # print(' '.join(map(str, ans)))
        # print(*ans)
    else:
        list.append(boxes[query[1] - 1])
        # print(' '.join(map(str, boxes[query[1] - 1])))
        # print(*boxes[query[1] - 1])

for i in range(len(list)):
    print(list[i])