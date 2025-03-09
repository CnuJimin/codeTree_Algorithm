n ,t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2)]

up = arr[0]
down = arr[1]

temp_u = 0
temp_d = 0 


for _ in range(t):
    temp_u = up[n - 1]

    for i in range(n-1, 0, -1):
        up[i] = up[i-1]

    up[0] = down[n - 1]

    for i in range(n-1, 0 , -1):
        down[i] = down[i-1]

    down[0] = temp_u

print(*up)
print(*down)