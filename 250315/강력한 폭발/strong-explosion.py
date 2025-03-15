#배열을 돌면서 1이 있는 경우에 모든 폭탄 방식을 다해봄..

n = int(input())

#폭탄이 주어진 위치 
arr = [list(map(int, input().split())) for i in range(n)]

#폭탄이 터진 범위 
bomb_arr = [[0 for i in range(n)] for i in range(n)]
bomb_pos = []

bomb_num = 0 

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 :
            bomb_pos.append((i,j))
            bomb_num += 1 




def getArea(arr):
    cnt = 0 
    for i in arr:
        for j in i:
            if j == 1 :
                cnt += 1
    
    return cnt


def initialBombArr():
    global bomb_arr
    bomb_arr = [[0 for i in range(n)] for i in range(n)]


def in_range(x,y):
    return 0<=x<n and 0<=y<n

def boom(x,y,n):
    if n == 1 :
        dx = [-2,-1,0,1,2]
        dy = [0, 0, 0, 0, 0]

        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]

            if in_range(nx,ny):
                bomb_arr[nx][ny] = 1 
    
    if n == 2:
        dx = [-1,0,0,0,1]
        dy = [0, -1, 0, 1, 0]

        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]

            if in_range(nx,ny):
                bomb_arr[nx][ny] = 1 

    if n == 3:
        dx = [-1,-1,0,1,1]
        dy = [-1, 1,0, -1,1]

        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]

            if in_range(nx,ny):
                bomb_arr[nx][ny] = 1 




        


answer = -1 

def backtrack(num):
    global answer, bomb_arr

    if num == bomb_num:
        #폭탄이 터진 범위의 합을 구함 
        area = getArea(bomb_arr)

        answer = max(answer, area)
        return 

    
    for i in range(1, 4):
        x,y = bomb_pos[num]
        backup = [row[:] for row in bomb_arr]  


        boom(x,y,i)
        backtrack(num + 1)
        bomb_arr = backup

backtrack(0)

print(answer)