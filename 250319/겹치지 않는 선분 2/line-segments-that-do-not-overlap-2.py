#선분이 겹치게 되는 기준 -> x2가 그 전 수의 x2보다 앞에 있을 때 겹침
# 선분을 정렬하고, 자기보다 앞에 있는 선분들의 x2 값의 최댓값 기준으로 그것보다 앞에 있으면 겹치는 선분 

n = int(input())
x = [] 
y = [] 

for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
# lines = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    overlap = False
    for j in range(n):
        if i == j : 
            continue 
        
        if (x[i] <= x[j] and y[i] >= y[j]) or (x[i] >= x[j] and y[i] <=  y[j]) :
            overlap = True 
            break
        
    if overlap :
        ans += 1

print(ans)