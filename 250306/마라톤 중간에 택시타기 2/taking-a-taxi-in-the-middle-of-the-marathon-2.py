import sys

N = int(input())

x = []
y = []

answer = sys.maxsize
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

# 1과 N을 제외한 모든 N의 각 지점 i에 대해서 
for i in range(1, N - 1):
    dist = 0
    # i를 제외했을 때 거리를 구해 abs(x1 - x2) + abs(y1 - y2) 최단 거리를 갱신한다 
    n_x = x[:i] + x[i+1:]
    n_y = y[:i] + y[i+1:]

    for j in range(N - 2):
        dist += abs(n_x[j] - n_x[j + 1]) + abs(n_y[j] - n_y[j + 1])
    answer = min(answer, dist)

print(answer)