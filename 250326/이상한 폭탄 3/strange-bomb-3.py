n, k = map(int, input().split())

bombs = [int(input()) for _ in range(n)]

bomb = [0] * 1000001
visited = [0] * n 

# print(*bombs)
for i in range(n-k):
    for j in range(i+1,i+k+1):
        # print(i,j)
        if bombs[i] == bombs[j] :
            if visited[i] == 0 :
                visited[i] = 1
                bomb[bombs[i]] += 1
            if visited[j] == 0:
                visited[j] = 1
                bomb[bombs[j]] += 1
            # print(i,j)

# print(*bomb[0:25])

max_value = max(bomb)

result = [] 

for i in range(1000001):
    if bomb[i] == max_value:
        result.append(i)

# print(*result)

if max_value == 0 :
    print(0)
else:
    print(max(result))

