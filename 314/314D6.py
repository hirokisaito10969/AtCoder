def main():
    N = int(input())
    S = list(input().strip())
    Q = int(input())
    
    operations = []
    last_type_2_or_3 = None
    
    for _ in range(Q):
        t, x, c = input().split()
        t = int(t)
        x = int(x)
        operations.append((t, x, c))
        
        if t == 1:
            S[x - 1] = c
        elif t == last_type_2_or_3:
            apply_operation(S, t)
    
    print("".join(S))

def apply_operation(S, op_type):
    if op_type == 2:
        S[:] = [char.lower() for char in S]
    elif op_type == 3:
        S[:] = [char.upper() for char in S]

if __name__ == "__main__":
    main()
