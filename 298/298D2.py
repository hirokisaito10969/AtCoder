# from atcoder.modint import modint998244353
# mint = modint998244353

class mint:
    def __init__(self, x):
        self.x = x % 998244353

    def __add__(self, other):
        if isinstance(other, mint):
            return mint(self.x + other.x)
        return mint(self.x + other)

    def __sub__(self, other):
        if isinstance(other, mint):
            return mint(self.x - other.x)
        return mint(self.x - other)

    def __mul__(self, other):
        if isinstance(other, mint):
            return mint(self.x * other.x)
        return mint(self.x * other)

    def __pow__(self, other):
        if isinstance(other, mint):
            return mint(self.x ** other.x)
        return mint(self.x ** other)

    def __truediv__(self, other):
        if isinstance(other, mint):
            return mint(self.x * pow(other.x, 998244351, 998244353))
        return mint(self.x * pow(other, 998244351, 998244353))

    def __str__(self):
        return str(self.x)

    def __repr__(self):
        return repr(self.x)

def main():
    import sys
    input = sys.stdin.readline

    Q = int(input())
    
    S = [1]
    ans = mint(1)
    
    for i in range(Q):
        t, = map(int, input().split())
        if t==1:
            x, = map(int, input().split())
            S.append(x)
            ans = ans*10 + x
        elif t==2:
            ans -= mint(10).pow(len(S)-1) * S[0]
            S.pop(0)
        elif t==3:
            print(ans.x)
    
    return 0

if __name__ == "__main__":
    main()
