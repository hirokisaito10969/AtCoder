dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    
    if s[0][0] != 's':
        print("No")
        return
    
    next = {}
    next['s'] = 'n'
    next['n'] = 'u'
    next['u'] = 'k'
    next['k'] = 'e'
    next['e'] = 's'
    
    seen = [[False] * w for _ in range(h)]
    
    def dfs(i, j):
        seen[i][j] = True
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if s[ni][nj] != next[s[i][j]]:
                continue
            if seen[ni][nj]:
                continue
            dfs(ni, nj)
    
    dfs(0, 0)
    print("Yes" if seen[h - 1][w - 1] else "No")

if __name__ == "__main__":
    main()
