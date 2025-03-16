n = int(input())

arr = [list(map(int, input().split()))for _ in range(n)]

ans = 0 

for i in range(n):
    for j in range(n-2):
        area = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        ans = max(ans, area)

print(ans)