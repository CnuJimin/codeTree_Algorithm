# 19 * 19 배열을 만들어서 input을 받아둠 
# 배열에서 2~17 2~17 까지 탐색하면서, 그 수를 기준으로 좌우 2칸 대각선 2칸에 모두 같은 수가 있으면 그 수가 이긴 거

arr = [list(map(int, input().split())) for _ in range(19)]

winner = 0 
mid_x, mid_y = 0, 0 
for x in range(2, 17):
    for y in range(2, 17):
        #새로로 이겼을 때 
        if arr[x-2][y] + arr[x-1][y] + arr[x][y] + arr[x+1][y] + arr[x+2][y] == 5:
            winner = 1
            mid_x, mid_y = x, y 

        elif arr[x-2][y] + arr[x-1][y] + arr[x][y] + arr[x+1][y] + arr[x+2][y] == 10:
            winner = 2 
            mid_x, mid_y = x, y 

        
        #가로로 이겼을 때 
        if arr[x][y-2] + arr[x][y-1] + arr[x][y] + arr[x][y+1] + arr[x][y+2] == 5:
            winner = 1
            mid_x, mid_y = x, y 

        elif arr[x][y-2] + arr[x][y-1] + arr[x][y] + arr[x][y+1] + arr[x][y+2] == 10:
            winner = 2 
            mid_x, mid_y = x, y 


        #대각선으로 이겼을 때 
        if arr[x-2][y-2] + arr[x-1][y-1] + arr[x][y] + arr[x+1][y+1] + arr[x+2][y+2] == 5:
            winner = 1
            mid_x, mid_y = x, y 

        elif arr[x-2][y-2] + arr[x-1][y-1] + arr[x][y] + arr[x+1][y+1] + arr[x+2][y+2] == 10:
            winner = 2 
            mid_x, mid_y = x, y 


if winner == 0 : 
    print(winner)
else:
    print(winner)
    print(mid_x + 1, mid_y + 1)
