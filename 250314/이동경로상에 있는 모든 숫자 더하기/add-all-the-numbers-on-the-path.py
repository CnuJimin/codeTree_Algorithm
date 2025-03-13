# 시작 위치 n//2 + 1 

n,  t = map(int, input().split())

moveList = list(input())

x, y = n//2, n//2 

arr = [list(map(int, input().split())) for i in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dist_num = 3

ans = 0 

ans += arr[x][y]

def in_range(x,y):
    return 0<= x <n and 0 <= y < n 


for i in range(t):
    
    way = moveList[i]

    if way == "R":
        dist_num = (dist_num + 1) % 4 
    elif way == "L":
        dist_num = (dist_num + 3) % 4 
    elif way == "F":
        nx, ny = x + dx[dist_num], y + dy[dist_num]
        if in_range(nx,ny):
            ans += arr[nx][ny]
            x, y = nx, ny
    # print(x,y)



print(ans)




