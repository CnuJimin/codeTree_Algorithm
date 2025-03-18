n,t,h = map(int, input().split())

height = list(map(int, input().split()))

for i in range(n):
    height[i] = abs(height[i] - h)

height.sort()

ans = 0 
for i in range(t):
    ans += height[i]

print(ans)