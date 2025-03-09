n, m, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

marble = [tuple(map(int, input().split())) for _ in range(m)]

#구슬의 각 위치에 대해서 

count_arr = [[0 for i in range(n)]for i in range(n)]
next_count_arr = [[0 for i in range(n)]for i in range(n)]


def in_range(x,y):
    return 0<=x<n and 0<=y<n

def get_max_neighbor(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    max_num, max_pos = 0, (0,0)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx,ny) and arr[nx][ny] > max_num:
            max_num = arr[nx][ny]
            max_pos = (nx,ny)
    return max_pos


def move(x, y):
    nx, ny = get_max_neighbor(x,y)
    next_count_arr[nx][ny] += 1



def move_all():
    #next_count 배열 초기화 
    for i in range(n):
        for j in range(n):
            next_count_arr[i][j] = 0

    #
    for i in range(n):
        for j in range(n):
            if count_arr[i][j] == 1:
                move(i, j)

    for i in range(n):
        for j in range(n):
            count_arr[i][j] = next_count_arr[i][j]




def remove_marble():
    for i in range(n):
        for j in range(n):
            if count_arr[i][j] != 1:
                count_arr[i][j] = 0


def simulate():
    move_all()

    remove_marble()




for i in range(m):
    x, y = marble[i]
    x, y = x-1 , y-1

    count_arr[x][y] = 1


for _ in range(t):
    simulate()


cnt = 0

for i in range(n):
    for j in range(n):
        cnt += count_arr[i][j]





print(cnt)