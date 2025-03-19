import sys

n,h,t = map(int, input().split())

height = list(map(int, input().split()))

ans = sys.maxsize

for i in range(n-t): 
    total = 0 
    for j in range(t):
        total += abs(h-height[i + j])
    
    ans = min(ans, total)


print(ans)