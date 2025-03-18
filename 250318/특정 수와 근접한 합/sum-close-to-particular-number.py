import sys
n, s = map(int, input().split())

nums = list(map(int, input().split()))


ans = sys.maxsize

for i in range(n-1):
    for j in range(i+1, n):
        survive = []
        for k in range(n):
            if k == i or k == j :
                continue
            survive.append(nums[k])

        ans = min(ans, abs(s-sum(survive)))


print(ans)