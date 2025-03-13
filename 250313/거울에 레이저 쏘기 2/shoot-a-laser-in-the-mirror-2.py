# 거울을 만났을 때 출발하는 방향에 따라 꺾이는 방향이 다름 이를 구별해둬야 할듯 
# 0, 1, 2, 3 기준으로 
# => / 거울 만나면 어느 방향이든 -1 dist = (dist + 3) % 4 
# => \ 거울 만나면 어느 방향이든 + 1 dist = (dist + 1) % 4 

# 총 12번 진행해서, 나가지 않고 거울에 팅기면 횟수를 하나 더해줌 
# 거울의 크기 자체를 [n+2][n+2]로 잡고 가운데 n*n에 거울을 넣어둠 
# 시작 위치를 k를 어떻게 잡아야 할 것인가.. k -  // n 을 사분면

n = int(input())

#거울을 담을 배열 생성 
arr = [[0 for i in range(n+2)] for i in range(n + 2)]

#거울 채우기 
for i in range(1, n+1):
    mirror = list(input())
    for j in range(1, n+1):
        arr[i][j] = mirror[j-1]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

k = int(input())

x, y = 0, 0
dist_num = 0 
if k <= n :
    x,y = 0, k 
    dist_num = 1 
elif k <= 2*n:
    x, y = k-n, n + 1
    dist_num = 2
elif k <= 3*n:
    x, y = n+1, 3*n + 1 - k 
    dist_num = 3
elif k <= 4*n:
    x, y = 4*n + 1 - k , 0
    dist_num = 0

ans = 0 

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

while True:
    nx = x + dx[dist_num]
    ny = y + dy[dist_num]

    #만약 다음 좌표가 범위 밖이라면 그만 
    if not in_range(nx,ny):
        break

    #다음 좌표에 어떤 거울이 있는지 확인 
    if arr[nx][ny] == "/":
        dist_num = (dist_num + 3) % 4 
    else:
        dist_num = (dist_num + 1) % 4 
    
    x, y = nx, ny 
    ans += 1

print(ans)