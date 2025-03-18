
# 19 * 19 배열을 만들어서 input을 받아둠 
# 배열에서 2~17 2~17 까지 탐색하면서, 그 수를 기준으로 좌우 2칸 대각선 2칸에 모두 같은 수가 있으면 그 수가 이긴 거

# arr = [list(map(int, input().split())) for _ in range(19)]

# winner = 0 
# mid_x, mid_y = 0, 0 


# # 성공한 모양에 따라서 for 문 범위를 다르게 해줘야 함 
# for x in range(15):
#     for y in range(19):
#         if arr[x][y] == arr[x+1][y] == arr[x+2][y] == arr[x+3][y] == arr[x+4][y] == 1:
#             winner = 1
#             mid_x, mid_y = x+2, y 

#         elif arr[x][y] == arr[x+1][y] == arr[x+2][y] == arr[x+3][y] == arr[x+4][y] == 2:
#             winner = 2 
#             mid_x, mid_y = x+2, y 


# for x in range(19):
#     for y in range(15):
#         if arr[x][y] == arr[x][y+1] == arr[x][y+2] == arr[x][y+3] == arr[x][y+4] == 1:
#             winner = 1
#             mid_x, mid_y = x, y+2

#         elif arr[x][y] == arr[x][y+1] == arr[x][y+2] == arr[x][y+3] == arr[x][y+4] == 2:
#             winner = 2 
#             mid_x, mid_y = x, y+2


# for x in range(15):
#     for y in range(15):
#         if arr[x][y] == arr[x+1][y+1] == arr[x+2][y+2] == arr[x+3][y+3] == arr[x+4][y+4] == 1:
#             winner = 1
#             mid_x, mid_y = x+2, y+2

#         elif arr[x][y] == arr[x+1][y+1] == arr[x+2][y+2] == arr[x+3][y+3] == arr[x+4][y+4] == 2:
#             winner = 2 
#             mid_x, mid_y = x+2, y+2 

# for x in range(4,19):
#     for y in range(15):
#         if arr[x][y] == arr[x-1][y+1] == arr[x-2][y+2] == arr[x-3][y+3] == arr[x-4][y+4] == 1:
#             winner = 1
#             mid_x, mid_y = x-2, y-2 

#         elif arr[x][y] == arr[x-1][y+1] == arr[x-2][y+2] == arr[x-3][y+3] == arr[x-4][y+4] == 2:
#             winner = 2 
#             mid_x, mid_y = x-2, y+2 



# if winner == 0 : 
#     print(winner)
# else:
#     print(winner)
#     print(mid_x + 1, mid_y + 1)


import sys

arr = [list(map(int, input().split()))for i in range(19)]

dx = [0, 1, 1, 1, 0, -1 ,-1 ,-1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def in_range(x,y):
    return 0 <= x < 19 and 0 <= y < 19

for i in range(19):
    for j in range(19):

        if arr[i][j] == 0 :
            continue 
        
        for k in range(8):
            cur_x = i 
            cur_y = j 
            cur_t = 1

            while True :
                nx = cur_x + dx[k]
                ny = cur_y + dy[k]

                if not in_range(nx, ny):
                    break 
                
                if arr[nx][ny] != arr[cur_x][cur_y]:
                    break 
                
                cur_x = nx
                cur_y = ny 
                cur_t += 1

                if cur_t == 5:
                    print(arr[i][j])
                    print(i + 2 * dx[k] + 1, j + 2 * dy[k] + 1)
                    sys.exit()

            
print(0)

    
