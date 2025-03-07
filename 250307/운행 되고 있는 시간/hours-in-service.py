N = int(input())

workHour = [0] * 1010 

arr = [tuple(map(int, input().split())) for _ in range(N)]

for a, b in arr:
    for j in range(a, b):
        workHour[j] = 1

# 모든 시간 i에 대해서 

answer = 0

for i in range(N):
    cnt = 0
    a, b = arr[i]
    # 해당 시간 j가 빠졌을 때의 운영시간을 구해 최댓값을 갱신한다 
    for j in range(a,b - 1):
        workHour[j] = 0
    
    for j in workHour:
        if j == 1 :
            cnt += 1
    
    answer = max(answer, cnt)

    for j in range(a,b - 1):
        workHour[j] = 1
    


print(answer + 1)