N = int(input())

same_flavor = [[] for _ in range(N + 1)]
flavor_list = []

for i in range(N):
    F, S = map(int, input().split())
    same_flavor[F].append(S)
    if F not in flavor_list:
        flavor_list.append(F)

max_satisfaction = 0

for flavor_group in same_flavor:
    flavor_group.sort(reverse=True)

# print (flavor_list)
for i in range (len(flavor_list)-1):
    flavor_list_i =flavor_list[i]
    if len(same_flavor[flavor_list_i]) >= 2:
        flavor_group_max = same_flavor[flavor_list_i][0] + same_flavor[flavor_list_i][1] // 2
        max_satisfaction = max(max_satisfaction, flavor_group_max)

    for j in range(i+1,len(flavor_list)):
        flavor_list_j =flavor_list[j]
        if len(same_flavor[flavor_list_j]) >= 1:
            flavor_group_with_max = same_flavor[flavor_list_i][0] + same_flavor[flavor_list_j][0]
            max_satisfaction = max(max_satisfaction, flavor_group_with_max)

print(max_satisfaction)

# 16 AC 8 WA 29 TLE