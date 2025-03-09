n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0 
# j 0~n-3
for i in range(n - 2):
    for j in range(n - 2):
        total = 0 

        for k in range(3):
            for h in range(3):
                total += arr[i + k][j + h]


        ans = max(ans, total)

print(ans)