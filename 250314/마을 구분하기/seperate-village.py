n = int(input())

town = []

graph = [list(map(int, input().split())) for i in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and graph[x][y] == 1 and visited[x][y] == 0 


def dfs(x,y):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if can_go(nx,ny):
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx,ny)

    
    return cnt


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0 :
            cnt = 1
            visited[i][j] = 1
            town.append(dfs(i,j))


# for i in range(n):
#     for j in range(n):
#         print(visited[i][j], end = " ")
#     print()



town.sort()

print(len(town))
for i in town:
    print(i)