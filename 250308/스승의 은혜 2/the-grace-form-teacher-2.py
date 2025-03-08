n, b = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()

ans = 0

for i in range(n):
    total = 0
    cnt = 0
    for j in range(n):
        if j == i :
            if (total + arr[j]//2) <= b:
                total += arr[j] // 2
                cnt += 1
                continue

        if (total + arr[j]) <= b:
            total += arr[j]
            cnt += 1
        else:
            break
    
    ans = max(cnt, ans)

print(ans)