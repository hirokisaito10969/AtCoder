def main():
    N = int(input())
    people = []
    
    for _ in range(N):
        C = int(input())
        A = list(map(int, input().split()))
        people.append((C, A))
    
    X = int(input())
    
    min_bet_count = float('inf')
    candidates = []
    
    for i, (C, A) in enumerate(people, start=1):
        if X in A:
            if C < min_bet_count:
                min_bet_count = C
                candidates = [i]
            elif C == min_bet_count:
                candidates.append(i)
    
    print(len(candidates))
    if candidates:
        print(*candidates)

if __name__ == "__main__":
    main()
