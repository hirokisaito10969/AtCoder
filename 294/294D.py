import bisect

N, Q = map(int, input().split())
called = [0] * N
waiting = []
results = []

for i in range(Q):
    event = input().split()
    if event[0] == "1":
        if len(waiting) > 0:
            p = waiting.pop(0)
        else:
            p = bisect.bisect_left(called, 0)
        called[p] = 1
        results.append(p+1)
    elif event[0] == "2":
        x = int(event[1]) - 1
        called[x] = 1
        bisect.insort_left(waiting, x)
    else:
        p = bisect.bisect_left(called, 1)
        called[p] = 2
        results.append(p+1)

for res in results:
    print(res)
    