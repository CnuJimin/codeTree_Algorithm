#배열 크기 200_010
#가운데서 시작해서 N번 명령을 받음 
#명령을 받을 때 R,L을 확인해서 이동할 방향을 수정해줌 
#이동하면서 색을 칠해줌, B는 +1, W는 +2, 만약 배열의 크기가 6이상이면 -1로 값을 바꿈 O(nx + 배열의 크기)?? 

arr = [0] * 200010
white_arr = [0] * 200010
black_arr = [0] * 200010


#시작 위치 
x = 100050 

#R이면 dist_num = 0 , L이면 dist_num = 1

n = int(input())

for _ in range(n):
    dist, way = map(str, input().split())
    dist = int(dist)

    if way == "R" :
    #지금 자리 색칠, 
        arr[x] = 1
        black_arr[x] += 1
        #dist거리만큼 반복해서 이동 
        for i in range(dist - 1):
            x += 1
            arr[x] = 1
            black_arr[x] += 1
    
    else:
        arr[x] = 2
        white_arr[x] += 1
        #dist거리만큼 반복해서 이동 
        for i in range(dist - 1):
            x -= 1
            arr[x] = 2
            white_arr[x] += 1


    

black, white, gray = 0, 0, 0

#문제 발생 문제는 이게 더하는거라 당연히 값이 이게 아님 
for i in range(len(arr)):
    if black_arr[i] >= 2 and white_arr[i] >= 2:
        gray += 1
    elif arr[i] == 1:
        black += 1
    elif arr[i] == 2:
        white += 1

    
print(white, black, gray)
