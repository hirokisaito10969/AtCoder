N = int(input())
S = input()

takahashi_wins = S.count('T')
aoki_wins = N - takahashi_wins

if takahashi_wins > aoki_wins:
    print('T')
elif takahashi_wins < aoki_wins:
    print('A')
else:
    # 勝利数が同じ場合
    for i in range(N):
        if S[N-1-i] == 'T':
            takahashi_wins -= 1
        else:
            aoki_wins -= 1

        if takahashi_wins > aoki_wins:
            print('T')
            break
        elif takahashi_wins < aoki_wins:
            print('A')
            break
