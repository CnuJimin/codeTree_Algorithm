n, k = map(int, input().split())

bombs = [int(input()) for _ in range(n)]

bomb = [0] * 1000001
# 

# print(*bombs)
for i in range(n-k):
    for j in range(i+1,i+k+1):
        # print(i,j)
        if bombs[i] == bombs[j] :
            # print(i,j)
            bomb[bombs[i]] += 1
            # break

# print(*bomb[0:10])

max_value = max(bomb)

result = [] 

for i in range(n):
    if bomb[i] == max_value:
        result.append(i)

# print(*result)

if max_value == 0 :
    print(0)
else:
    print(max(result))

