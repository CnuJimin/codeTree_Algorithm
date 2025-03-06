n, k = map(int, input().split())

nums = list(map(int, input().split()))

# 모든 경우에 대해, 모든 i에 대해 n-k까지, N
dist = 0 
max_value = 0 
for i in range(n-k+1):
    # 할 거 한다 , i부터 k 까지의 합을 구하고 최댓값을 갱신한다 N -> O(N^2)
    dist = sum(nums[i:i+k])
    max_value = max(dist, max_value)

print(max_value)
