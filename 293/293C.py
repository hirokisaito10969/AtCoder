def solve():
    from itertools import combinations

    H,W=map(int,input().split())
    A=[None]*H

    for i in range(H):
        A[i]=list(map(int,input().split()))

    X=0
    for T in combinations(range(H+W-2), W-1):
        move=[0]*(H+W-2)
        for t in T:
            move[t]=1

        E={A[0][0]}
        i=j=0
        flag=1
        for t in range(H+W-2):
            if move[t]==0:
                i+=1
            else:
                j+=1
            if A[i][j] in E:
                flag=0
            E.add(A[i][j])
        X+=flag
    return X

#==================================================
print(solve())
