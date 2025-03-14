n, m = map(int, input().split())

graph = [[0 for i in range(n+1)] for i in range(n+1)]


for i in range(m):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0] * (n+1)

# vertex_cnt = 0 


def dfs(vertex):
    for curr_v in range(1, n+1):
        if graph[vertex][curr_v] == 1 and visited[curr_v] == 0:

                visited[curr_v] = 1
                # vertex_cnt += 1
                dfs(curr_v)



visited[1] = 1
dfs(1)


ans = 0 

for i in visited:
    if i == 1:
        ans += 1

print(ans -1)