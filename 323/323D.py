N = int(input().strip())

slimes = []
for _ in range(N):
    size, count = map(int, input().split())
    slimes.append((size, count))

slimes.sort()

i = 0
while i < len(slimes):
    size, count = slimes[i]
    while count > 1:
        count_org=count
        count //= 2
        size *= 2
        found = False
            
        for j in range(len(slimes)):
            if slimes[j][0] == size:
                slimes[j] = (size, slimes[j][1] + 1)
                found = True
                break
            
        if count_org % 2 ==0:
            del slimes[i]
        else:
            slimes[i] = (size, count_org - count * 2)
        if not found:
            slimes.append((size, 1))
            slimes.sort()
    i += 1

total_count = sum(count for size, count in slimes)

print(total_count)

# AC 4 WA 3 TLE 26