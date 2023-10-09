N = int(input())

cups = []
for _ in range(N):
    F, S = map(int, input().split())
    cups.append((F, S))

max_satisfaction = 0

for i in range(N):
    for j in range(i + 1, N):
        if i != j:
            s1, t1 = cups[i]
            s2, t2 = cups[j]
            
            if s1 != s2:
                satisfaction = t1 + t2
            else:
                satisfaction = max(t1,t2) + min(t1,t2) // 2
            
            max_satisfaction = max(max_satisfaction, satisfaction)

print(max_satisfaction)

# AC 8 TLE 45