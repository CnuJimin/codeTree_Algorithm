n, k = map(int, input().split())

bombs = [int(input()) for _ in range(n)]

bomb = [0] * 1000001

for i in range(n-k):
    for j in range(i+1,i+k+1):
        if bombs[i] == bombs[j] :
            bomb[i] += 1
            break

max_value = max(bomb)

result = [] 

for i in range(n):
    if bomb[i] == max_value:
        result.append(i)

if len(result) == 0 :
    print(0)
else:
    print(max(result))

