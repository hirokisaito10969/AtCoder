class Player:
    def __init__(self):
        self.yellow = 0  # イエローカードの提示回数
        self.red = False  # レッドカードの提示があったかどうか
        
    def receive_yellow(self):
        self.yellow += 1
        if self.yellow == 2:
            self.red = True
    
    def receive_red(self):
        self.red = True
    
    def is_disqualified(self):
        return self.red
    
n, q = map(int, input().split())
players = [Player() for _ in range(n)]

for _ in range(q):
    event, x = map(int, input().split())
    if event == 1:
        players[x-1].receive_yellow()
    elif event == 2:
        players[x-1].receive_red()
    else:
        print("Yes" if players[x-1].is_disqualified() else "No")
