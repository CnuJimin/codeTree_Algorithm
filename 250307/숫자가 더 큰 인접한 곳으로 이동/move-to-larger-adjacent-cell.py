n, x, y = map(int,input().split())
x, y = x -1, y - 1

arr = [list(map(int, input().split())) for i in range(n)]

dist_num = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x,y):
    return 0<= x < n and 0 <= y < n
print(arr[x][y], end = " ")

while True:
    flag = False
    for i in range(4):
        nx = x + dx[dist_num]
        ny = y + dy[dist_num]

        if in_range(nx, ny) and arr[nx][ny] > arr[x][y]:
            flag = True
            x = nx
            y = ny 

            print(arr[x][y], end = " ")

        dist_num = (dist_num + 1) % 4

    if not flag : 
        break
        

