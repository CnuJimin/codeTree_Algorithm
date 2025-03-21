n = int(input())
nums = list(map(int, input().split()))
nums.sort()


ans = 0 
#n개의 수 범위 안에서 k를 하나 잡고, 
for k in range(nums[0], nums[-1] + 1):
    cnt = 0 
    #nums 배열에서 수 두개를 정한 후, 각각 수와 k의 차이의 절댓값이 같으면 등차
    for i in range(n):
        for j in range(i+1, n):
            if abs(k - nums[i]) == abs(k-nums[j]):
                cnt += 1 
    
    ans = max(ans, cnt)

print(ans)