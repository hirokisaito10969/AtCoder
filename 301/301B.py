N = int(input())
A = list(map(int, input().split()))

i = 0
while i < len(A) - 1:
    if abs(A[i] - A[i+1]) == 1:
        i += 1
    else:
        if A[i] < A[i+1]:
            insert_nums = list(range(A[i]+1, A[i+1]))
        else:
            insert_nums = list(range(A[i]-1, A[i+1], -1))
        
        A[i+1:i+1] = insert_nums
        i += len(insert_nums) + 1

print(*A)
