# n, x, y = map(int,input().split())
# x, y = x -1, y - 1

# arr = [list(map(int, input().split())) for i in range(n)]

# dist_num = 0

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def in_range(x,y):
#     return 0<= x < n and 0 <= y < n

# print(arr[x][y], end = " ")

# while True:
#     flag = False
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if in_range(nx, ny) and arr[nx][ny] > arr[x][y]:
#             flag = True
#             print(nx, ny)
#             x = nx
#             y = ny 

#             print(arr[x][y], end = " ")

#             continue


#     if not flag : 
#         break
        

n, x, y = map(int,input().split())
x, y = x -1, y - 1

arr = [list(map(int, input().split())) for i in range(n)]

dist_num = 0


def in_range(x,y):
    return 0<= x < n and 0 <= y < n

def simulate(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if in_range(nx, ny) and arr[nx][ny] > arr[x][y]:
            return (nx, ny)
        
    return (-1,-1)




while True:
    print(arr[x][y] , end = " ")
    x, y = simulate(x,y)
    if x == -1 and y == -1 :
        break

