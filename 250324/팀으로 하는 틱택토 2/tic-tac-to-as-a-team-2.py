# #1~9의 수 중 2개를 선택함, 그리고 배열을 돌면서 해당 수가 있으면 그쪽으로 쭉 이동함 그리고 끝까지 갔을 때, 둘다 수가 등장한 횟수가 0이상이면 정답에 1을 더함 

# arr = [list(map(int, list(input()))) for _ in range(3)]

# # dx = [0, 1, 1, 1, 0, -1, -1, -1]
# # dy = [1, 1, 0, -1, -1, -1, 0, 1]

# dx = [0, 1, 1, 1]  # 오른쪽, 오른쪽 아래 대각선, 아래, 왼쪽 아래 대각선
# dy = [1, 1, 0, -1]  



# ans = 0 

# def in_range(x,y):
#     return 0<=x<3 and 0<=y<3

# #2개의 수 선택 
# for i in range(1, 10):
#     for j in range(1, 10):
#         if i == j :
#             continue
#         #배열을 돌면서 수를 찾음 
#         for x in range(3):
#             for y in range(3):
#                 if arr[x][y] != i or arr[x][y] != j:
#                     continue 

#                 for n in range(4):
#                     cx = x
#                     cy = y
#                     a_num = 0 
#                     b_num = 0 


#                     while True :
#                         if not in_range(cx,cy):
#                             break

#                         if arr[cx][cy] == i :
#                             a_num += 1 
#                         elif arr[cx][cy] == j :
#                             b_num += 1
#                         else:
#                             break


#                         cx += dx[n]
#                         cy += dy[n]
        
#                     if a_num + b_num == 3 and a_num!=0 and b_num != 0 :
#                         ans += 1 

# print(ans)
        

arr = [list(map(int, list(input()))) for _ in range(3)]

dx = [0, 1, 1, 1]  # 오른쪽, 오른쪽 아래 대각선, 아래, 왼쪽 아래 대각선
dy = [1, 1, 0, -1]  

ans = 0 

def in_range(x, y):
    return 0 <= x < 3 and 0 <= y < 3

# 2개의 숫자 선택 
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
        
        # 배열을 돌면서 특정 숫자를 포함한 경우만 탐색
        for x in range(3):
            for y in range(3):
                if arr[x][y] != i and arr[x][y] != j:
                    continue  # 현재 칸이 i 또는 j가 아니라면 탐색할 필요 없음
                
                # 4가지 방향으로 탐색 (중복 세기 방지)
                for n in range(4):
                    cx, cy = x, y
                    a_num, b_num = 0, 0  

                    for _ in range(3):  # 3칸 이동해야 승리 조건 성립
                        if not in_range(cx, cy):
                            break  # 범위를 벗어나면 종료
                        
                        if arr[cx][cy] == i:
                            a_num += 1
                        elif arr[cx][cy] == j:
                            b_num += 1
                        else:
                            break  # 둘 중 하나가 아니면 연속되지 않으므로 종료
                        
                        cx += dx[n]
                        cy += dy[n]
                    
                    # 3개의 칸이 연속으로 i, j로만 구성되어 있고, 둘 다 포함해야 함
                    if a_num + b_num == 3 and a_num > 0 and b_num > 0:
                        ans += 1

print(ans//2)