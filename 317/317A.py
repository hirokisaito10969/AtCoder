def find_weakest_effective_potion(N, H, X, potions):
    weakest_potion = None
    
    for i in range(N):
        if X <= H + potions[i]:
            if weakest_potion is None or potions[i] < potions[weakest_potion]:
                weakest_potion = i
    
    return weakest_potion + 1
    
N, H, X = map(int, input().split())
potions = list(map(int, input().split()))

result = find_weakest_effective_potion(N, H, X, potions)
print(result)
