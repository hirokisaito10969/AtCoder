def fireworks_count(N, M, A):
    fireworks_days = [0] * (N + 1)
    
    for i in range(M):
        fireworks_days[A[i]] = 1
    
    days_until_fireworks = [0] * (N + 1)
    current_countdown = N
    for i in range(N, 0, -1):
        if fireworks_days[i] == 1:
            current_countdown = 0
        days_until_fireworks[i] = current_countdown
        current_countdown += 1
    
    for i in range(1, N + 1):
        print(days_until_fireworks[i])

N, M = map(int, input().split())
A = list(map(int, input().split()))

fireworks_count(N, M, A)
