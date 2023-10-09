N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# 睡眠時間の合計を計算する関数
def calculate_sleep_time(l, r):
    sleep_time = 0

    # l から r までの区間で睡眠をとっている時間を加算する
    for i in range(1, N, 2):
        start = A[i]
        end = A[i + 1]

        # 区間が [start, end] と [l, r] で重なっている場合に睡眠時間を計算する
        if end >= l and start <= r:
            sleep_start = max(start, l)
            sleep_end = min(end, r)
            sleep_time += sleep_end - sleep_start

    return sleep_time

list1 = []
# 各質問に対して睡眠時間を計算して出力する
for _ in range(Q):
    l, r = map(int, input().split())
    sleep_time = calculate_sleep_time(l, r)
    # print(sleep_time)
    list1.append(sleep_time)
    
for i in range(Q):
    print(list1[i])
