#N번의 반복문(1~N) 동안 N이 홀수이면 빨강, 짝수이면 파란색으로 색을 칠함 
arr = [[0 for i in range(221)]for i in range(221)]

n = int(input())

for num in range(1, n+1):
    # 빨간색으로 칠할 때 
    if num % 2 != 0 :
        x1,y1,x2,y2 = map(int, input().split())
        x1,y1,x2,y2 = x1 + 110,y1 + 110,x2 + 110,y2 + 110

        for x in range(x1,x2):
            for y in range(y1,y2):
                arr[x][y] = 1


    #파란색으로 칠할 때 
    if num % 2 == 0 :
        x1,y1,x2,y2 = map(int, input().split())
        x1,y1,x2,y2 = x1 + 110,y1 + 110,x2 + 110,y2 + 110

        for x in range(x1,x2):
            for y in range(y1,y2):
                arr[x][y] = 2


answer = 0 

for i in range(221):
    for j in range(221):
        if arr[i][j] == 2:
            answer += 1

print(answer)