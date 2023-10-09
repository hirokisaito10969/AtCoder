def main():
    N = int(input())
    S = list(input().strip())
    Q = int(input())
    
    operations = []
    
    last_type_2_index = -1
    last_type_3_index = -1
    
    for i in range(Q):
        t, x, c = input().split()
        t = int(t)
        x = int(x)
        operations.append((t, x, c))
        
        if t == 2:
            last_type_2_index = i
        elif t == 3:
            last_type_3_index = i
    
    last_type_index = max(last_type_2_index, last_type_3_index)
    
    if last_type_index == last_type_2_index:
        last_type = 2
    else:
        last_type = 3
    
    for t, x, c in operations:
        if t == 1:
            S[x - 1] = c
        elif t == last_type:
            apply_operation(S, t)
    
    print("".join(S))

def apply_operation(S, op_type):
    if op_type == 2:
        S[:] = [char.lower() for char in S]
    elif op_type == 3:
        S[:] = [char.upper() for char in S]

if __name__ == "__main__":
    main()

# 18 TLE