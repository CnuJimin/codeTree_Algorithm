n = int(input())

nums = list(map(int, input().split()))


ans = 0 

for i in range(n):
    for j in range(i, n):
        avr = sum(nums[i:j+1]) / (j-i+1)
        if avr in nums[i:j+1]:
            ans += 1

print(ans)