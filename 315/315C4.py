N = int(input())

cups = []
for _ in range(N):
    F, S = map(int, input().split())
    cups.append((F, S))
    
# 美味しさSで降順にソート
cups.sort(key=lambda x: x[1], reverse=True)


max_satisfaction = 0
found_same_flavor = False
same_flavor = True

for i in range(1,N):
    s1, t1 = cups[0]
    s2, t2 = cups[i]
    
    if s1 != s2:
        satisfaction = t1 + t2
    elif same_flavor:
        satisfaction = max(t1, t2) + min(t1, t2) // 2
        same_flavor = False
    
    max_satisfaction = max(max_satisfaction, satisfaction)
    
    if s1 != s2:
        found_same_flavor = True
        break
        
    
print(max_satisfaction)

# AC