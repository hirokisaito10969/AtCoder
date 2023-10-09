import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# 区間ごとの睡眠時間を事前に計算する
sleep_times = []
for i in range(1, N, 2):
    start = A[i]
    end = A[i + 1]
    sleep_time = end - start
    sleep_times.append(sleep_time)

list1 = []
# 各クエリの睡眠時間を計算して出力する
for _ in range(Q):
    l, r = map(int, input().split())
    
    a = bisect.bisect_right(A, l)
    b = bisect.bisect_right(A, r)
    
    print(a)
    print(b)
    
    sleepl = 0
    sleepr = 0
    
    if a % 2 == 0 and b % 2 == 0:
        sleepl = sleep_times[a//2-1] + l - A[a]
        sleepr = sleep_times[b//2-1] + r - A[b]
        sleepa = 0
        for i in range(a//2 + 1, b//2):
            sleepa += sleep_times[i-1]
        sleep=sleepl+sleepr+sleepa
    elif a % 2 == 0 and b % 2 == 1:
        # sleep = sleep_times[b // 2]  - sleep_times[a // 2]+ l - A[a - 1]
        sleepl = sleep_times[a//2-1] + l - A[a]
        sleepr = sleep_times[b//2]
        sleepa = 0
        for i in range(a//2 + 1, b//2):
            sleepa += sleep_times[i-1]
    elif a % 2 == 1 and b % 2 == 0:
        sleep = sleep_times[b // 2]+ r - A[b] - sleep_times[(a - 1) // 2] 
    elif a % 2 == 1 and b % 2 == 1:
        if((a-1)//2)==0:
            sleepl=0
        else:
            sleepl = sleep_times[a//2-1]
        for i in range (b//2-1):
            sleepr += sleep_times[i]
        # sleepr = sleep_times[b//2-1]
        sleep=sleepr-sleepl
    
    print(sleepl)
    print(sleepr)
    
    list1.append(sleep)

for i in range(Q):
    print(list1[i])
