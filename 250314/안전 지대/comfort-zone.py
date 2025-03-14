n, m = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(n)]


def in_range(x,y):
    return 0<=x<n and 0<=y<m


def can_go(x,y,k):
    return in_range(x,y) and graph[x][y] > k and visited[x][y] == 0 


def dfs(x,y,k):
    global cnt
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if can_go(nx,ny,k):
            visited[nx][ny] = 1 
            dfs(nx,ny,k)

    

answer = []



for k in range(1, 101):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > k and visited[i][j] == 0 :
                cnt += 1
                visited[i][j] = 1 
                dfs(i,j,k)


    answer.append((k, cnt))


answer.sort(key = lambda x : -x[1])

print(answer[0][0], answer[0][1])