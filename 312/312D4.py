MOD = 998244353

class Mint:
    def __init__(self, val):
        self.val = val % MOD

    def __add__(self, other):
        if isinstance(other, Mint):
            return Mint(self.val + other.val)
        return Mint(self.val + other)

    def __sub__(self, other):
        if isinstance(other, Mint):
            return Mint(self.val - other.val)
        return Mint(self.val - other)

    def __mul__(self, other):
        if isinstance(other, Mint):
            return Mint(self.val * other.val)
        return Mint(self.val * other)

def main():
    s = input()
    n = len(s)
    dp = [[Mint(0) for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = Mint(1)

    for i in range(n):
        for j in range(n):
            if s[i] != ')':
                dp[i + 1][j + 1] += dp[i][j]
            if j != 0 and s[i] != '(':
                dp[i + 1][j - 1] += dp[i][j]

    print(dp[n][0].val)

if __name__ == "__main__":
    main()
