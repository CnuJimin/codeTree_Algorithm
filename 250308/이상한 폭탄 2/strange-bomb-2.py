n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

ans = -1

#각 폭발 i에 대해
for i in range(n-k):
    search = arr[i:i+k+1]
    #k범위 안에 동일한 폭탄이 존재하는지 확인 
    if len(search) != len(set(search)):
        ans = max(ans, max(search))
    


print(ans)