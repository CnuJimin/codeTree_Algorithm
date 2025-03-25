n, k = map(int, input().split())

nums = [int(input()) for _ in range(n)]
ans = 0 
#1부터 10_000까지의 수 중에서 최솟값i 을 일단 정하고, 
for i in range(1, 10001):
    cnt = 0 
    select = [] 
    for j in range(n):
        if i <= nums[j] <= i + k:
            select.append(nums[j])
    
    cnt = len(select)
    ans = max(ans, cnt)

print(ans)
#배열을 돌면서, i와 i +k 사이에 있으면 선택한 뒤, 배열의 길이를 세면 됨, 그리고 최댓값 갱신 