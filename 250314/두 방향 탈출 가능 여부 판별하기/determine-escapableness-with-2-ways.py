n, m = map(int, input().split())

#배열 만들어주기 
graph = [list(map(int, input().split())) for _ in range(n)]

#방문 여부 배열 만들어주기 
visited = [[0 for _ in range(m)] for _ in range(n)]

order = 1

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and graph[x][y] != 0 and visited[x][y] == 0 

#dfs 함수 만들기 
def dfs(x, y):
    global order

    graph[x][y] = order

    dx = [1, 0]
    dy = [0, 1]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if can_go(nx,ny):
            visited[nx][ny] = 1
            order += 1
            dfs(nx,ny)



visited[0][0] = 1

dfs(0,0)


# for i in range(n):
#     for j in range(n):
#         print(graph[i][j], end = " ")
#     print()

# print("**********")

# for i in range(n):
#     for j in range(n):
#         print(visited[i][j], end = " ")
#     print()


if graph[n-1][m-1] == 1 :
    print("0")
else:
    print("1")





