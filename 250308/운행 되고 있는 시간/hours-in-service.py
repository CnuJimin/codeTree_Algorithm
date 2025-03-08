N = int(input())

workHour = [0] * 1010 

arr = [tuple(map(int, input().split())) for _ in range(N)]

#미리 색을 칠하면 안됨 

answer = 0

#i번째 근무 시간을 생략함
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        a, b = arr[j]
        for k in range(a,b):
            workHour[k] = 1
    for j in workHour:
        if j == 1:
            cnt += 1
    answer = max(answer, cnt)
    workHour = [0] * 1010 

        


print(answer)