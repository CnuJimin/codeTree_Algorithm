import sys 
n = int(input())

spot = [list(map(int, input().split())) for _ in range(n)]

#n개중 2개의 점을 선택해서 두 점 사이의 거리를 구함 
ans = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        x1,y1 = spot[i]
        x2,y2 = spot[j]
        

        ans = min(ans, abs((x1-x2) * (x1-x2))  + abs((y1-y2) * (y1-y2)))

#최소가 되는 두 점을 가지고 두 점 사이의 거리의 제곱을 구힘 

print(ans)