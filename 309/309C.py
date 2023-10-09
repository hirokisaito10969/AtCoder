N, K = map(int, input().split())
medicines = []
for _ in range(N):
    a, b = map(int, input().split())
    medicines.append((a, b))

day = 1
while True:
    total = 0
    for a, b in medicines:
        if a >= day:
            total += b
        if total > K:
            break
    
    if total < K:
        break
    
    day += 1

print(day)
