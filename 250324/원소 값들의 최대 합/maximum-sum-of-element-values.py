n, m = map(int, input().split())

nums = list(map(int, input().split()))

#모든 nums에 대해서, 해당 자리에의 수를 더한 후, 인덱스로 이동하고, 해당 값을 더하고 인덱스로 이동하는 것을 m번 반복 
ans = 0 


for i in range(n):
    result = 0 
    nx = nums[i]
    for _ in range(m):
        result += nx
        nx = nums[nx - 1]
    
    ans = max(ans, result)

print(ans)
