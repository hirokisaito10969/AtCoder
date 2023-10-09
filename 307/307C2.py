import sys
sys.setrecursionlimit(10**9)

def can_achieve_goal(HA, WA, A, HB, WB, B, HX, WX, X):
    sheetC = [['.' for _ in range(WA)] for _ in range(HA + HB)]

    def dfs(x, y):
        if x == HA + HB:
            return check_match()

        nx, ny = (x + 1) % (HA + HB), y + (x + 1) // (HA + HB)
        if nx >= HA:
            nx -= HA
            if y + 1 >= WA - WB + 1:
                return False

        # Place sheet A
        sheetC[x][y] = A[x % HA][y]
        if dfs(nx, ny):
            return True

        # Place sheet B
        sheetC[x][y] = B[x % HB][y]
        if dfs(nx, ny):
            return True

        return False

    def check_match():
        for i in range(HA + HB - HX + 1):
            for j in range(WA - WX + 1):
                if is_matching_region(i, j):
                    return True
        return False

    def is_matching_region(start_row, start_col):
        for i in range(HX):
            for j in range(WX):
                if sheetC[start_row + i][start_col + j] == '#' and X[i][j] != '#':
                    return False
        return True

    return "Yes" if dfs(0, 0) else "No"


# Read input
HA, WA = map(int, input().split())
A = [input() for _ in range(HA)]
HB, WB = map(int, input().split())
B = [input() for _ in range(HB)]
HX, WX = map(int, input().split())
X = [input() for _ in range(HX)]

# Check if the goal can be achieved
result = can_achieve_goal(HA, WA, A, HB, WB, B, HX, WX, X)
print(result)
