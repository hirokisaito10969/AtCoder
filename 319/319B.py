def find_smallest_divisor(N):
    result = ""
    for i in range(N+1):
        found = False
        for j in range(1, 10):
            if N % j == 0 and i % (N // j) == 0:
                result += str(j)
                found = True
                break
        if not found:
            result += "-"
    return result

N = int(input())

result = find_smallest_divisor(N)
print(result)
