distances = {
    'A': 0,
    'B': 3,
    'C': 1,
    'D': 4,
    'E': 1,
    'F': 5,
    'G': 9
    }

p, q = input().split()

if p in distances and q in distances:
    if p == q:
        distance = 0
    elif p < q:
        distance = sum(distances[point] for point in distances if p < point <= q)
    else:
        distance = sum(distances[point] for point in distances if q < point <= p)
    print(distance)
