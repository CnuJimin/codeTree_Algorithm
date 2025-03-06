import sys 

N = int(input())

x = []
y = []

for _ in range(N):
    a ,b = map(int, input().split())
    x.append(a)
    y.append(b)

answer = sys.maxsize
#모든 N에 대해 i번째 좌표를 제외했을 때 -> N
for i in range(N):
    #가장 큰 x,y와 가장 작은 x,y를 구한다 -> 4N => o(n^2) 
    n_x = x[:i] + x[i+1:]
    n_y = y[:i] + y[i+1:]
    max_x = max(n_x)
    min_x = min(n_x)
    max_y = max(n_y)
    min_y = min(n_y)
    area = (max_x - min_x) * (max_y - min_y)

    answer = min(answer, area)

print(answer)