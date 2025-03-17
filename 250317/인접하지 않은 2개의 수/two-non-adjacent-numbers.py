n = int(input())

nums = list(map(int, input().split()))


ans = 0 
for i in range(n-2):
    for j in range(i+2, n):
        total = nums[i] + nums[j]
        ans = max(total, ans)

print(ans)