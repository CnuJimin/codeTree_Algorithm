n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

dx = [0, 1, 1, 1, 0, -1, -1, -1 ]
dy = [1, 1, 0, -1 ,-1 ,-1, 0,1]

ans = 0 

def in_range(x,y):
    return 0<=x<n and 0<=y<m

for i in range(n):
    for j in range(m):
        if arr[i][j] != "L":
            continue 
        
        for k in range(8):
            cx = i
            cy = j 
            ct = 1
            while True :
                nx = cx + dx[k]
                ny = cy + dy[k]

                if not in_range(nx,ny):
                    break
                
                if arr[nx][ny] != "E":
                    break
                
                cx = nx
                cy = ny 
                ct += 1

                if ct == 3 :
                    ans += 1 
                    break

print(ans)