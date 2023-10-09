N = int(input().strip())

slimes = []
for _ in range(N):
    size, count = map(int, input().split())
    slimes.append((size, count))

slimes.sort()

i = 0
slime_count = 0
while i < len(slimes):
    size, count = slimes[i]
    if count % 2 == 1:
        slime_count += 1
    # while count > 1:
    count //= 2
    size *= 2
    found = False
        
    for j in range(len(slimes)):
        if slimes[j][0] == size:
            slimes[j] = (size, slimes[j][1] + count)
            found = True
            break
        
    if not found:
        slimes.append((size, 1))
        slimes.sort()
    i += 1

print(slime_count)

# AC 4 WA 3 TLE 26