N, M = map(int, input().split())

sets = []
count1 = 0
countM = 0

for _ in range(N):
    set_elements = set(map(int, input().split()[1:]))
    sets.append(set_elements)
    if 1 in set_elements:
        count1 += 1
    if M in set_elements:
        countM += 1

if count1 == 0 or countM == 0:
    print(-1)
elif count1 > 0 and countM > 0:
    print(2)
else:
    print(1)
