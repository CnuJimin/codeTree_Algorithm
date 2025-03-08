n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

ans = -1

#각 폭발 i에 대해
for i in range(n-k):
    search = arr[i:i+k+1]
    #k범위 안에 동일한 폭탄이 존재하는지 확인 
    for j in range(k+1):
        for t in range(k+1):
            if j == t :
                continue
            #동일한 폭탄이 존재한다면 해당 폭탄의 번호를 저장
            if search[j] == search[t]:
                boom = search[j]
                ans = max(ans, boom)
    
    


print(ans)