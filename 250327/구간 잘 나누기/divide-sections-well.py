# 7 2 1 5 6 3 
# n개의 수가 주어지면 n-1 개 중에서 m-1개를 선택함
# m-1개를 선택하려면 반복문을 m-1 번 돌면서, 하나씩 선택하는데, 방문 여부를 확인함..? 

n, m = map(int, input().split())

nums = list(map(int, input().split()))


ans = 10000

for i in range(1, 10001):
    possible = True 
    cnt = 0 
    section = 1
    for j in range(n):

        if nums[j] > i :
            possible = False
            break
        
        if cnt + nums[j] > i:
            cnt = 0 
            section += 1
        
        cnt += nums[j]
    
    if possible and section <= m :
        ans = min(ans, i)

print(ans)

        