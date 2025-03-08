n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

ans = -1

for i in range(n):
    for j in range(i+1, n):
        if j - i > k :
            break
        
        if arr[i] != arr[j] :
            continue
        
        ans = max(ans, arr[i])

print(ans)