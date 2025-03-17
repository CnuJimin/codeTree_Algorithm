import sys

n = int(input())
room = [int(input()) for _ in range(n)]

#방을 이동할 때 더 높은 수로 이동해야함, 자기보다 작은 수로 가면 n에서 큰수에서 작은수를 뺀 값이 거리 

# 배열을 만드러서 각 방에 몇명이 들어가야 하는지 기록한다. 
# 방을 하나씩 지정해서, 각 방에서 다른 방으로의 이동 거리와 그 방에 가야하는 사람의 수를 곱한다.

ans = sys.maxsize

for i in range(n): #처음 모일 방의 위치 
    dist = 0 

    for j in range(n): #이동할 방의 위치 
        if i > j :
            dist += room[j] * (n - (i - j))
        else:
            dist += room[j] * (j-i)

    ans = min(dist, ans)

# 이를 다 더하고 어떤 방에서 시작하는 것이 최솟값인지 구한다. 
print(ans )