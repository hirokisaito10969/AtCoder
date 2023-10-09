def solve_election(N, data):
    sorted_data = sorted(data, key=lambda x: x[2], reverse=True)
    
    seat_taka = 0
    seat_aoki = 0
    
    to_win_list = []
    
    for i in range(N):
        if sorted_data[i][0] > sorted_data[i][1]:
            seat_taka += sorted_data[i][2]
        else:
            seat_aoki += sorted_data[i][2]
            to_win_list.append(((sorted_data[i][1] - sorted_data[i][0] + 1) // 2, sorted_data[i][2], sorted_data[i][2] / (sorted_data[i][1] - sorted_data[i][0] + 1)*2))
            
    sa = seat_aoki - seat_taka
    num = 0
    if sa < num:
        return num
    else:
        to_win_listttt = sorted(to_win_list, key=lambda x: x[2], reverse=True)
        for i in range(len(to_win_listttt)):
            num += to_win_listttt[i][0]
            seat_aoki -= to_win_listttt[i][1]
            seat_taka += to_win_listttt[i][1]
            sa = seat_aoki - seat_taka
            if sa < num:
                return num
        return num
                
N = int(input())
data = []
for _ in range(N):
    X, Y, Z = map(int, input().split())
    data.append((X, Y, Z))

answer = solve_election(N, data)
print(answer)

# AC 13 WA 22
# 平均でソートするのは良い考えだと思ったがだめそう。
# for で回して最小値を取得するしかないのか、、