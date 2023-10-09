S = input()

result = ''.join(c for c in S if c not in ['a', 'e', 'i', 'o', 'u'])

print(result)
