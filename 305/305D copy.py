class SegmentTree:
    def __init__(self, data):
        n = len(data)
        self.size = 1 << n.bit_length()
        self.tree = [0] * (2 * self.size)
        for i in range(n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, left, right):
        result = 0
        left += self.size
        right += self.size
        while left < right:
            if left & 1:
                result += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result


N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# 区間ごとの睡眠時間を計算しておく
sleep_times = []
for i in range(1, N, 2):
    sleep_start = A[i]
    sleep_end = A[i + 1]
    sleep_time = sleep_end - sleep_start
    sleep_times.append(sleep_time)

# セグメントツリーを構築する
segment_tree = SegmentTree(sleep_times)

list1 = []
# 各質問に対してセグメントツリーを利用して睡眠時間を取得して出力する
for _ in range(Q):
    l, r = map(int, input().split())
    sleep_time = segment_tree.query((l - 1) // 2, r // 2)
    # print(sleep_time)

    list1.append(sleep_time)
    
for i in range(Q):
    print(list1[i])