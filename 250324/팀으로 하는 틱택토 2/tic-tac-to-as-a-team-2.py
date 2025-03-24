#1~9의 수 중 2개를 선택함, 그리고 배열을 돌면서 해당 수가 있으면 그쪽으로 쭉 이동함 그리고 끝까지 갔을 때, 둘다 수가 등장한 횟수가 0이상이면 정답에 1을 더함 

arr = [list(map(int, list(input()))) for _ in range(3)]

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]


ans = 0 

def in_range(x,y):
    return 0<=x<3 and 0<=y<3

#2개의 수 선택 
for i in range(1, 10):
    for j in range(1, 10):
        if i == j :
            continue
        #배열을 돌면서 수를 찾음 
        for x in range(3):
            for y in range(3):
                cx = x
                cy = y
                a_num = 0 
                b_num = 0 

                if arr[x][y] == i or arr[x][y] == j:
                    if arr[x][y] == i :
                        a_num += 1 
                    else:
                        b_num += 1

                    for n in range(8):
                        while True :

                            nx = cx + dx[n]
                            ny = cy + dy[n]

                            if not (in_range(nx,ny) and (arr[nx][ny] == i or arr[nx][ny] == j)):
                                break

                            cx = nx 
                            cy = ny 

                            if arr[cx][cy] == i :
                                a_num += 1 
                            else:
                                b_num += 1


        
        if a_num + b_num == 3 and a_num!=0 and b_num != 0 :
            ans += 1 

print(ans)
        

