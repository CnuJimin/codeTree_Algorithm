#n개의 빙산을 기록해두고
#1~1000까지의 범위를 돌면서 해당 값을 빙산에 빼고, 0보다 작아지면 0으로 표시해둠, 
#그리고 배열을 다시 돌면서, 연속으로 1인 구간을 체크함 

n = int(input())

arr = [int(input()) for _ in range(n)]

ans = 0 
#해수면의 높이 설정 
for i in range(1, 1001):
    cnt = 0 
    ice = arr[:]
    #해수면 높이 조정 
    for j in range(n):
        ice[j] -= i 
    
    #높이 조정 이후 빙산 덩어리 체크 
    chunk = False
    for j in range(n):
        #덩어리 구하는 로직 
        if ice[j] > 0 :
            if not chunk:
                cnt += 1
                chunk = True
        else:
            chunk = False


    ans = max(ans, cnt)
print(ans)